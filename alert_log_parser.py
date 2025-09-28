#!/usr/bin/env python3
"""
alert_log_parser.py

Usage:
    python alert_log_parser.py <logfile> [--json]

Features:
- Groups Oracle alert log lines into entries (based on timestamp lines).
- Extracts ORA- error codes and counts them per entry.
- Prints a human-readable summary, with optional JSON output.
"""

import re
import sys
import json
from pathlib import Path
from typing import List, Dict

# Oracle alert logs start with day-of-week prefixes
DAY_PREFIXES = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Regex to capture ORA- error codes
ORA_RE = re.compile(r"(ORA-\d{5})")


def parse_alert_log(path: Path) -> List[str]:
    """Read a log file and group lines into entries based on timestamp lines."""
    with path.open("r", encoding="utf-8", errors="ignore") as fh:
        lines = fh.readlines()

    entries: List[str] = []
    current: List[str] = []

    for line in lines:
        # Detect a new entry by day-of-week prefix
        if line.startswith(DAY_PREFIXES):
            if current:
                entries.append("".join(current).strip())
                current = []
        current.append(line)

    if current:
        entries.append("".join(current).strip())

    return entries


def extract_ora_counts(entry: str) -> Dict[str, int]:
    """Return a dict with counts for each ORA- code in the entry and a total count."""
    codes = ORA_RE.findall(entry)
    counts: Dict[str, int] = {}
    for c in codes:
        counts[c] = counts.get(c, 0) + 1
    counts["__total__"] = len(codes)
    return counts


def summarize(entries: List[str]) -> List[Dict]:
    """Create a summary dict per entry: timestamp, snippet, ora_counts."""
    summary = []
    for idx, entry in enumerate(entries, 1):
        first_line = entry.splitlines()[0] if entry else ""
        ora_counts = extract_ora_counts(entry)
        snippet = "\n".join(entry.splitlines()[:5])  # preview
        summary.append({
            "entry_id": idx,
            "timestamp": first_line,
            "snippet": snippet,
            "ora_counts": ora_counts,
            "raw": entry,
        })
    return summary


def print_human(summary: List[Dict]):
    """Print a human-readable summary of log entries."""
    for item in summary:
        total = item["ora_counts"].get("__total__", 0)
        print(f"--- Entry {item['entry_id']} --- ({total} ORA- errors)")
        print(item["snippet"])
        if total > 0:
            print("Full ORA counts:")
            for k, v in item["ora_counts"].items():
                if k == "__total__":
                    continue
                print(f"  {k}: {v}")
        print()


def main(argv):
    if len(argv) < 2:
        print("Usage: python alert_log_parser.py <logfile> [--json]")
        return 2

    path = Path(argv[1])
    to_json = "--json" in argv or "-j" in argv

    if not path.exists():
        print(f"File not found: {path}")
        return 2

    entries = parse_alert_log(path)
    summary = summarize(entries)

    if to_json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"Total entries found: {len(entries)}\n")
        print_human(summary)

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))

