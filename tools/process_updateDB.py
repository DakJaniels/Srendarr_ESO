#!/usr/bin/env python3
"""
Process Srendarr:FullUpdate() SavedVariables dump into minorEffects / majorEffects patches.

Usage (from repo root):
  python tools/process_updateDB.py path/to/Srendarr.lua
  python tools/process_updateDB.py path/to/SrendarrDB.lua --aura-data Srendarr/Srendarr/AuraData.lua

After /script Srendarr:FullUpdate() completes, ReloadUI, then point this script at
SavedVariables/Srendarr.lua (or a pasted extract of the updateDB table).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ENTRY_RE = re.compile(r"\[(\d+)\]\s*=\s*(EFFECT_\w+)\s*,")
AURA_ENTRY_RE = re.compile(r"\[(\d+)\]\s*=\s*(EFFECT_\w+)\s*,")
HIGHLIGHT_EFFECTS = ("EFFECT_VEXATION", "EFFECT_PROPHECY", "EFFECT_SORCERY")

UPDATEDB_KEYS = (
    "MinorAdded",
    "MinorRemoved",
    "MajorAdded",
    "MajorRemoved",
)


def extract_braced_block(text: str, start_index: int) -> tuple[str, int] | None:
    """Return inner contents of the `{ ... }` starting at start_index, and end index."""
    open_brace = text.find("{", start_index)
    if open_brace < 0:
        return None
    depth = 0
    for index in range(open_brace, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[open_brace + 1 : index], index
    return None


def find_update_db_blocks(text: str) -> list[str]:
    """Find all ['updateDB'] / updateDB = { ... } blocks, including nested tables."""
    blocks: list[str] = []
    pattern = re.compile(r"(?:\[['\\\"]updateDB['\\\"]\]|updateDB)\s*=\s*\{")
    for match in pattern.finditer(text):
        extracted = extract_braced_block(text, match.start())
        if extracted:
            blocks.append(extracted[0])
    return blocks


def parse_effect_bucket(block: str, key: str) -> dict[str, list[tuple[int, str]]]:
    """Parse MinorAdded/etc keyed by effect display name -> list of (id, EFFECT_*)."""
    key_pattern = re.compile(
        rf"(?:\[['\\\"]{re.escape(key)}['\\\"]\]|{re.escape(key)})\s*=\s*\{{"
    )
    key_match = key_pattern.search(block)
    if not key_match:
        return {}

    extracted = extract_braced_block(block, key_match.start())
    if not extracted:
        return {}

    bucket_text, _ = extracted
    results: dict[str, list[tuple[int, str]]] = {}

    name_pattern = re.compile(r"\[['\\\"]([^'\\\"]+)['\\\"]\]\s*=\s*\{")
    for name_match in name_pattern.finditer(bucket_text):
        effect_name = name_match.group(1)
        inner = extract_braced_block(bucket_text, name_match.start())
        if not inner:
            continue
        entries: list[tuple[int, str]] = []
        for entry_match in ENTRY_RE.finditer(inner[0]):
            entries.append((int(entry_match.group(1)), entry_match.group(2)))
        if entries:
            results[effect_name] = entries
    return results


def count_entries(parsed: dict[str, dict[str, list[tuple[int, str]]]]) -> int:
    total = 0
    for bucket in parsed.values():
        for entries in bucket.values():
            total += len(entries)
    return total


def parse_update_db(text: str) -> dict[str, dict[str, list[tuple[int, str]]]]:
    best: dict[str, dict[str, list[tuple[int, str]]]] = {key: {} for key in UPDATEDB_KEYS}
    best_count = 0

    for block in find_update_db_blocks(text):
        parsed = {key: parse_effect_bucket(block, key) for key in UPDATEDB_KEYS}
        entry_count = count_entries(parsed)
        if entry_count > best_count:
            best = parsed
            best_count = entry_count

    return best


def parse_current_effects(aura_data_path: Path) -> tuple[dict[int, str], dict[int, str]]:
    text = aura_data_path.read_text(encoding="utf-8")
    minor_match = re.search(r"^minorEffects\s*=\s*\{(.*?)^majorEffects\s*=", text, re.DOTALL | re.MULTILINE)
    major_match = re.search(
        r"^majorEffects\s*=\s*\{(.*?)(?:^--------------------------------------------------------------------------------------------------------------------|^local )",
        text,
        re.DOTALL | re.MULTILINE,
    )
    if not minor_match or not major_match:
        raise SystemExit(f"Could not find minorEffects/majorEffects in {aura_data_path}")

    def collect(block: str) -> dict[int, str]:
        found: dict[int, str] = {}
        for match in AURA_ENTRY_RE.finditer(block):
            found[int(match.group(1))] = match.group(2)
        return found

    return collect(minor_match.group(1)), collect(major_match.group(1))


def format_lua_line(ability_id: int, effect_name: str) -> str:
    return f"    [{ability_id}] = {effect_name},"


def print_bucket(
    title: str,
    bucket: dict[str, list[tuple[int, str]]],
    current: dict[int, str],
) -> None:
    print(f"=== {title} ===")
    if not bucket:
        print("(empty)")
        print()
        return

    for effect_name in sorted(bucket.keys()):
        entries = sorted(bucket[effect_name], key=lambda item: item[0])
        highlight = ""
        for _, effect_const in entries:
            if effect_const in HIGHLIGHT_EFFECTS:
                highlight = f"  [{effect_const}]"
                break
        print(f"-- {effect_name}{highlight} ({len(entries)})")
        for ability_id, effect_const in entries:
            already = ""
            if title.endswith("Added") and ability_id in current:
                already = f"  -- already in table as {current[ability_id]}"
            elif title.endswith("Removed") and ability_id not in current:
                already = "  -- not in current table"
            print(f"{format_lua_line(ability_id, effect_const)}{already}")
        print()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    default_aura_data = repo_root / "Srendarr" / "Srendarr" / "AuraData.lua"

    parser = argparse.ArgumentParser(
        description="Convert FullUpdate updateDB dump into minorEffects/majorEffects Lua lines."
    )
    parser.add_argument(
        "dump_path",
        type=Path,
        help="SavedVariables/Srendarr.lua or SrendarrDB.lua",
    )
    parser.add_argument(
        "--aura-data",
        type=Path,
        default=default_aura_data,
        help=f"AuraData.lua path (default: {default_aura_data})",
    )
    args = parser.parse_args()

    if not args.dump_path.is_file():
        print(f"Dump file not found: {args.dump_path}", file=sys.stderr)
        return 1
    if not args.aura_data.is_file():
        print(f"AuraData.lua not found: {args.aura_data}", file=sys.stderr)
        return 1

    dump_text = args.dump_path.read_text(encoding="utf-8", errors="replace")
    parsed = parse_update_db(dump_text)
    if count_entries(parsed) == 0:
        print(
            "No updateDB Added/Removed entries found. Run /script Srendarr:FullUpdate(), "
            "ReloadUI, then pass SavedVariables/Srendarr.lua.",
            file=sys.stderr,
        )
        return 1

    minor_current, major_current = parse_current_effects(args.aura_data)

    print("=== Summary ===")
    for key in UPDATEDB_KEYS:
        total = sum(len(entries) for entries in parsed[key].values())
        print(f"{key}: {total} IDs across {len(parsed[key])} effect names")
    print()

    print_bucket("MinorAdded", parsed["MinorAdded"], minor_current)
    print_bucket("MinorRemoved", parsed["MinorRemoved"], minor_current)
    print_bucket("MajorAdded", parsed["MajorAdded"], major_current)
    print_bucket("MajorRemoved", parsed["MajorRemoved"], major_current)

    print("Review Vexation adds and Prophecy/Sorcery removes before pasting into AuraData.lua.")
    print("Keep Sun Fire DO NOT REMOVE rows unless the dump lists those IDs as removed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
