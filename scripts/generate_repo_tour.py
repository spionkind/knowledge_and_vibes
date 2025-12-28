#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class FileEntry:
    path: str
    kind: str
    title: str | None
    description: str | None
    meta: dict[str, Any]


@dataclass(frozen=True)
class ExcludedPath:
    path: str
    reason: str


def _strip_wrapping_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> list[str] | None:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    parts = [p.strip() for p in inner.split(",")]
    return [_strip_wrapping_quotes(p) for p in parts if p]


def _parse_front_matter(markdown_text: str) -> tuple[dict[str, Any], str]:
    if not markdown_text.startswith("---\n"):
        return {}, markdown_text

    # Find the closing '---' line.
    lines = markdown_text.splitlines(keepends=True)
    fm_lines: list[str] = []
    end_index: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break
        fm_lines.append(lines[i])

    if end_index is None:
        return {}, markdown_text

    meta = _parse_simple_yaml("".join(fm_lines))
    body = "".join(lines[end_index + 1 :])
    return meta, body


def _parse_simple_yaml(yaml_text: str) -> dict[str, Any]:
    """
    Minimal YAML parser for frontmatter used in this repo.
    Supports:
      - key: value (strings; quotes optional)
      - key: [a, b, c] (inline lists)
      - key: (newline) followed by indented '- item' list
    """
    meta: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in yaml_text.splitlines():
        line = raw_line.rstrip("\n")
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("- "):
            if current_key is None:
                continue
            existing = meta.get(current_key)
            if not isinstance(existing, list):
                existing = []
                meta[current_key] = existing
            existing.append(_strip_wrapping_quotes(stripped[2:].strip()))
            continue

        match = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", stripped)
        if not match:
            continue

        key = match.group(1)
        value = match.group(2).strip()
        current_key = key

        if value == "":
            meta[key] = []
            continue

        inline_list = _parse_inline_list(value)
        if inline_list is not None:
            meta[key] = inline_list
            continue

        meta[key] = _strip_wrapping_quotes(value)

    return meta


def _first_markdown_heading(markdown_body: str) -> str | None:
    for raw_line in markdown_body.splitlines():
        line = raw_line.strip()
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            return match.group(2).strip()
    return None


def _first_markdown_paragraph(markdown_body: str) -> str | None:
    """
    Best-effort: return the first "paragraph" line after headings/frontmatter.
    """
    in_code = False
    paragraph_lines: list[str] = []

    for raw_line in markdown_body.splitlines():
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        # Code fences.
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        # Skip headings and structural lines.
        if not stripped:
            if paragraph_lines:
                break
            continue
        if re.match(r"^#{1,6}\s+", stripped):
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            continue
        if stripped.startswith("---"):
            continue

        paragraph_lines.append(stripped)
        if len(paragraph_lines) >= 3:
            break

    if not paragraph_lines:
        return None
    paragraph = " ".join(paragraph_lines).strip()
    paragraph = re.sub(r"\s+", " ", paragraph)
    return paragraph


def _read_text_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def _guess_kind(path: Path) -> str:
    if path.suffix.lower() == ".md" or path.name == "rules" or path.name in {"LICENSE", ".gitignore"}:
        return "markdown"
    if path.suffix.lower() == ".json":
        return "json"
    if path.suffix.lower() == ".sh":
        return "shell"
    return "other"


def _describe_special_file(rel_path: str) -> tuple[str | None, str | None, dict[str, Any]]:
    if rel_path == "LICENSE":
        return "License", "MIT license for this repository.", {}
    if rel_path == ".gitignore":
        return ".gitignore", "Ignore rules: cloned tool repos, local AI configs, editor/temp artifacts.", {}
    return None, None, {}


def _extract_pipeline_stages(repo_root: Path) -> list[str]:
    guide_path = repo_root / "docs" / "workflow" / "IDEATION_TO_PRODUCTION.md"
    text = _read_text_file(guide_path)
    if text is None:
        return []
    _, body = _parse_front_matter(text)
    stages: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^###\s+Stage\s+(-?\d+)\s+—\s+(.+)$", line.strip())
        if match:
            stages.append(f"Stage {match.group(1)} — {match.group(2).strip()}")
    return stages


def _walk_repo(repo_root: Path, output_rel: str) -> tuple[list[FileEntry], list[ExcludedPath]]:
    ignore_dirs = {
        ".git",
        ".bv_backups",
        ".tmp_gocache",
        ".tmp_gomodcache",
        "__pycache__",
    }
    ignore_files = {".DS_Store"}
    output_rel_norm = output_rel.strip().lstrip("./")

    entries: list[FileEntry] = []
    excluded: list[ExcludedPath] = []

    for dirpath, dirnames, filenames in os.walk(repo_root, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]

        for filename in filenames:
            if filename in ignore_files:
                continue

            full_path = Path(dirpath) / filename
            rel_path = full_path.relative_to(repo_root).as_posix()

            if rel_path == output_rel_norm:
                continue

            kind = _guess_kind(full_path)
            title: str | None = None
            description: str | None = None
            meta: dict[str, Any] = {}

            special_title, special_desc, special_meta = _describe_special_file(rel_path)
            if special_title or special_desc or special_meta:
                title, description, meta = special_title, special_desc, special_meta
            else:
                if kind in {"markdown", "json", "shell", "other"}:
                    text = _read_text_file(full_path)
                    if text is None:
                        entries.append(
                            FileEntry(
                                path=rel_path,
                                kind="binary",
                                title=None,
                                description="Binary/unreadable as UTF-8; excluded from content summary.",
                                meta={},
                            )
                        )
                        continue

                    if kind == "markdown":
                        fm, body = _parse_front_matter(text)
                        meta.update(fm)
                        title = (
                            fm.get("title")
                            or fm.get("name")
                            or _first_markdown_heading(body)
                            or full_path.name
                        )
                        description = (
                            fm.get("description")
                            or _first_markdown_paragraph(body)
                            or None
                        )
                    elif kind == "json":
                        title = full_path.name
                        description = "JSON configuration."
                        # Avoid heavy parsing; just expose top-level keys if possible.
                        try:
                            import json

                            obj = json.loads(text)
                            if isinstance(obj, dict):
                                meta["keys"] = sorted(obj.keys())
                        except Exception:
                            pass
                    elif kind == "shell":
                        title = full_path.name
                        description = "Shell script."
                    else:
                        title = full_path.name
                        description = None

            entries.append(
                FileEntry(
                    path=rel_path,
                    kind=kind,
                    title=title,
                    description=description,
                    meta=meta,
                )
            )

    # Record excluded dirs at a high level for transparency.
    for d in sorted(ignore_dirs):
        if (repo_root / d).exists():
            excluded.append(ExcludedPath(path=d + "/", reason="Ignored (git/caches/backups)."))
    return entries, excluded


def _group_key(rel_path: str) -> str:
    if rel_path in {"README.md", "START_HERE.md", "GLOSSARY.md", "TEMPLATES.md"}:
        return "Root: Orientation"
    if rel_path.startswith("docs/workflow/"):
        return "Docs: Workflow"
    if rel_path.startswith("docs/guides/"):
        return "Docs: Guides"
    if rel_path.startswith("templates/"):
        return "Templates (Operator-Facing)"
    if rel_path.startswith(".claude/commands/"):
        return ".claude: Slash Commands"
    if rel_path.startswith(".claude/skills/"):
        return ".claude: Skills (and Subagents)"
    if rel_path.startswith(".claude/rules/"):
        return ".claude: Rules"
    if rel_path.startswith(".claude/templates/"):
        return ".claude: Runtime Templates"
    if rel_path.startswith("research/"):
        return "Research Summaries"
    if rel_path.startswith(".codex/") or rel_path.startswith(".cursor/") or rel_path.startswith(".gemini/"):
        return "Other AI Tooling"
    if rel_path.startswith("docs/"):
        return "Docs: Other"
    return "Other Files"


def _render_markdown(repo_root: Path, entries: list[FileEntry], excluded: list[ExcludedPath]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    stages = _extract_pipeline_stages(repo_root)

    by_group: dict[str, list[FileEntry]] = {}
    for e in entries:
        by_group.setdefault(_group_key(e.path), []).append(e)

    group_order = [
        "Root: Orientation",
        "Docs: Workflow",
        "Docs: Guides",
        "Templates (Operator-Facing)",
        ".claude: Slash Commands",
        ".claude: Rules",
        ".claude: Skills (and Subagents)",
        ".claude: Runtime Templates",
        "Other AI Tooling",
        "Research Summaries",
        "Docs: Other",
        "Other Files",
    ]

    out: list[str] = []
    out.append("---")
    out.append("title: Repo Tour (Generated)")
    out.append("description: File-by-file walkthrough of Knowledge & Vibes: purpose, workflow, tools, and agent configuration.")
    out.append("---")
    out.append("")
    out.append("# Knowledge & Vibes — Repo Tour (Generated)")
    out.append("")
    out.append(f"_Generated at {now} by `scripts/generate_repo_tour.py`._")
    out.append("")
    out.append("## What This Project Is")
    out.append("")
    out.append(
        "Knowledge & Vibes is a research-backed framework for building software with AI. "
        "It formalizes planning (North Star + REQ/AC + ADRs), decomposes work into "
        "**beads** (tracked tasks with dependencies), coordinates multiple agents via "
        "Agent Mail (messaging + file reservations), and enforces verification gates "
        "(TDD-first tests, iteration caps, and security scanning via `ubs`)."
    )
    out.append("")
    out.append("## Workflow (10-Stage Pipeline)")
    out.append("")
    if stages:
        for s in stages:
            out.append(f"- {s}")
    else:
        out.append("- See `docs/workflow/IDEATION_TO_PRODUCTION.md` for the complete pipeline.")
    out.append("")
    out.append("## How To Use This Repo (Fast Path)")
    out.append("")
    out.append("- Start: `README.md`")
    out.append("- Orientation hub: `START_HERE.md`")
    out.append("- Workflow reference: `docs/workflow/IDEATION_TO_PRODUCTION.md` and `docs/workflow/PROTOCOLS.md`")
    out.append("- Practical tooling: `docs/guides/TUTORIAL.md`")
    out.append("- Templates: `TEMPLATES.md` and `templates/`")
    out.append("- Evidence: `research/README.md`")
    out.append("")
    out.append("## File-by-File Walkthrough")
    out.append("")

    def fmt_entry(e: FileEntry) -> str:
        bits: list[str] = [f"`{e.path}`"]
        if e.title:
            bits.append(f"— {e.title}")
        line = " ".join(bits)
        if e.description:
            line += f": {e.description}"
        return line

    for group in group_order:
        items = by_group.get(group, [])
        if not items:
            continue
        out.append(f"### {group}")
        out.append("")
        for e in sorted(items, key=lambda x: x.path):
            out.append(f"- {fmt_entry(e)}")
        out.append("")

    if excluded:
        out.append("## Excluded Paths")
        out.append("")
        for ex in excluded:
            out.append(f"- `{ex.path}` — {ex.reason}")
        out.append("")

    out.append("## Regenerate")
    out.append("")
    out.append("```bash")
    out.append("python3 scripts/generate_repo_tour.py")
    out.append("```")
    out.append("")
    return "\n".join(out)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Generate a file-by-file repo tour Markdown document.")
    parser.add_argument(
        "--output",
        default="docs/REPO_TOUR.md",
        help="Output path (relative to repo root). Default: docs/REPO_TOUR.md",
    )
    args = parser.parse_args()

    output_rel = str(args.output)
    output_path = Path(output_rel)
    if not output_path.is_absolute():
        output_path = repo_root / output_path
    output_rel_norm = output_path.relative_to(repo_root).as_posix()

    entries, excluded = _walk_repo(repo_root=repo_root, output_rel=output_rel_norm)
    content = _render_markdown(repo_root, entries, excluded)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"Wrote {output_rel_norm} ({len(entries)} files indexed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

