#!/usr/bin/env python3
"""
Process Srendarr GetToggled() SavedVariables dump into toggledAuras Lua entries.

Usage (from repo root):
  python tools/process_toggled_dump.py path/to/Srendarr.lua
  python tools/process_toggled_dump.py path/to/toggled_lines.txt
  python tools/process_toggled_dump.py path/to/Srendarr.lua --aura-data Srendarr/Srendarr/AuraData.lua

Dump line format (from Srendarr.db.toggled):
  abilityId|abilityName||descriptionPrefix

After /script Srendarr:GetToggled() completes, ReloadUI, then point this script at
SavedVariables/Srendarr.lua (or a pasted extract of the toggled table).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FAKE_TOGGLE_ENTRIES = (
    (916007, "Sample Aura (FAKE)"),
    (916008, "Sample Aura (FAKE)"),
)

LINE_RE = re.compile(
    r"^\s*(?:\[\d+\]\s*=\s*)?[\"']?(\d+)\|([^|]+)\|\|([^\"']*)[\"']?\s*,?\s*$"
)
PLAIN_LINE_RE = re.compile(r"^(\d+)\|([^|]+)\|\|(.*)$")
AURA_ENTRY_RE = re.compile(
    r"\[(\d+)\]\s*=\s*true\s*,\s*--\s*(.+?)\s*$",
    re.MULTILINE,
)
TOGGLED_BLOCK_RE = re.compile(
    r"(local toggledAuras\s*=\s*\{)(.*?)(\n\})",
    re.DOTALL,
)


def parse_lines_from_text(search_text: str) -> dict[int, tuple[str, str]]:
    """Parse id|name||desc lines from a text blob. Returns id -> (name, desc)."""
    results: dict[int, tuple[str, str]] = {}
    fake_ids = {fake_id for fake_id, _ in FAKE_TOGGLE_ENTRIES}

    for raw_line in search_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("--"):
            continue

        match = LINE_RE.match(line) or PLAIN_LINE_RE.match(line)
        if not match:
            chat_match = re.match(r"^(\d+)\s+(\S.*?)\s{2,}(.*)$", line)
            if not chat_match:
                continue
            ability_id = int(chat_match.group(1))
            ability_name = chat_match.group(2).strip()
            ability_desc = chat_match.group(3).strip()
        else:
            ability_id = int(match.group(1))
            ability_name = match.group(2).strip()
            ability_desc = match.group(3).strip()

        if ability_id in fake_ids:
            continue
        results[ability_id] = (ability_name, ability_desc)

    return results


def parse_dump_text(text: str) -> dict[int, tuple[str, str]]:
    """Parse id|name||desc lines from SV snippet or plain text. Returns id -> (name, desc)."""
    block_pattern = re.compile(
        r"(?:\[['\\\"]toggled['\\\"]\]|toggled)\s*=\s*\{(.*?)\n\s*\}",
        re.DOTALL | re.IGNORECASE,
    )
    best_results: dict[int, tuple[str, str]] = {}
    for block_match in block_pattern.finditer(text):
        block_results = parse_lines_from_text(block_match.group(1))
        if len(block_results) > len(best_results):
            best_results = block_results

    if best_results:
        return best_results

    return parse_lines_from_text(text)


def parse_current_toggled_auras(aura_data_path: Path) -> dict[int, str]:
    """Read existing toggledAuras abilityID -> comment name from AuraData.lua."""
    text = aura_data_path.read_text(encoding="utf-8")
    block_match = TOGGLED_BLOCK_RE.search(text)
    if not block_match:
        raise SystemExit(f"Could not find toggledAuras block in {aura_data_path}")

    current: dict[int, str] = {}
    for match in AURA_ENTRY_RE.finditer(block_match.group(2)):
        ability_id = int(match.group(1))
        comment_name = match.group(2).strip()
        current[ability_id] = comment_name
    return current


def format_lua_entry(ability_id: int, ability_name: str) -> str:
    return f"    [{ability_id}] = true,  -- {ability_name}"


def build_lua_table(dump_entries: dict[int, tuple[str, str]]) -> str:
    """Emit a full toggledAuras body sorted by name then id, preserving FAKE samples."""
    rows: list[tuple[str, int, str]] = []
    for ability_id, (ability_name, _) in dump_entries.items():
        rows.append((ability_name.lower(), ability_id, ability_name))
    rows.sort(key=lambda row: (row[0], row[1]))

    lines = [
        "local toggledAuras =",
        "{                    -- there is a separate abilityID for every rank of a skill",
    ]
    for _, ability_id, ability_name in rows:
        lines.append(format_lua_entry(ability_id, ability_name))
    for fake_id, fake_name in FAKE_TOGGLE_ENTRIES:
        lines.append(format_lua_entry(fake_id, fake_name))
    lines.append("}")
    return "\n".join(lines) + "\n"


def print_diff(
    current: dict[int, str],
    dump_entries: dict[int, tuple[str, str]],
) -> None:
    fake_ids = {fake_id for fake_id, _ in FAKE_TOGGLE_ENTRIES}
    current_real = {ability_id for ability_id in current if ability_id not in fake_ids}
    dump_ids = set(dump_entries.keys())

    added = sorted(dump_ids - current_real)
    removed = sorted(current_real - dump_ids)
    kept = sorted(dump_ids & current_real)

    print("=== Diff vs current toggledAuras ===")
    print(f"kept:    {len(kept)}")
    print(f"added:   {len(added)}")
    print(f"removed: {len(removed)}  (review before deleting -- filters can miss edge cases)")
    print()

    if added:
        print("-- ADDED")
        for ability_id in added:
            ability_name, ability_desc = dump_entries[ability_id]
            desc_note = f"  |  {ability_desc}" if ability_desc else ""
            print(f"  {format_lua_entry(ability_id, ability_name)}{desc_note}")
        print()

    if removed:
        print("-- REMOVED (in AuraData, missing from dump)")
        for ability_id in removed:
            print(f"  {format_lua_entry(ability_id, current[ability_id])}")
        print()

    if not added and not removed:
        print("No ID changes vs current table (names may still differ).")
        print()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    default_aura_data = repo_root / "Srendarr" / "Srendarr" / "AuraData.lua"

    parser = argparse.ArgumentParser(
        description="Convert GetToggled dump into toggledAuras Lua + add/remove diff."
    )
    parser.add_argument(
        "dump_path",
        type=Path,
        help="SavedVariables/Srendarr.lua, SrendarrDB.lua, or plain id|name||desc text file",
    )
    parser.add_argument(
        "--aura-data",
        type=Path,
        default=default_aura_data,
        help=f"AuraData.lua path (default: {default_aura_data})",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write full toggledAuras Lua table to this file (also printed to stdout)",
    )
    args = parser.parse_args()

    if not args.dump_path.is_file():
        print(f"Dump file not found: {args.dump_path}", file=sys.stderr)
        return 1
    if not args.aura_data.is_file():
        print(f"AuraData.lua not found: {args.aura_data}", file=sys.stderr)
        return 1

    dump_text = args.dump_path.read_text(encoding="utf-8", errors="replace")
    dump_entries = parse_dump_text(dump_text)
    if not dump_entries:
        print(
            "No toggled dump lines found. Expected id|name||desc entries "
            "(or a ['toggled'] = { ... } block).",
            file=sys.stderr,
        )
        return 1

    current = parse_current_toggled_auras(args.aura_data)
    print_diff(current, dump_entries)

    lua_table = build_lua_table(dump_entries)
    print("=== Suggested toggledAuras table (review before pasting) ===")
    print(lua_table)

    if args.output:
        args.output.write_text(lua_table, encoding="utf-8")
        print(f"Wrote {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
