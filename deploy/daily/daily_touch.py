#!/usr/bin/env python3
"""Create a dated activity file and commit it to ensure a daily git update.

This script writes a small marker file into `checked/daily_edits/YYYY-MM-DD.md`
with a timestamp and an optional message, then commits and pushes the file.

It is intentionally conservative and only writes to the `checked/daily_edits/`
folder to avoid touching solution code.
"""
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CHECKED_DAILY = ROOT / "checked" / "daily_edits"


def ensure_dir():
    CHECKED_DAILY.mkdir(parents=True, exist_ok=True)


def write_marker(message: str | None = None) -> Path:
    today = datetime.utcnow().date().isoformat()
    fname = CHECKED_DAILY / f"{today}.md"
    now = datetime.utcnow().isoformat()
    content = f"# Daily edit for {today}\n\n- timestamp: {now} UTC\n"
    if message:
        content += f"- note: {message}\n"
    # if file exists, append a timestamp to avoid duplicate commits
    if fname.exists():
        content = fname.read_text() + f"\n- appended: {now} UTC\n"
    fname.write_text(content)
    return fname


def git_commit_and_push(path: Path) -> dict:
    try:
        subprocess.check_call(["git", "add", str(path)])
        subprocess.check_call(["git", "commit", "-m", f"chore(daily): touch {path.name}"])
        subprocess.check_call(["git", "push", "origin", "HEAD"])
        return {"ok": True}
    except subprocess.CalledProcessError as e:
        return {"ok": False, "error": str(e)}


def main():
    ensure_dir()
    msg = os.environ.get("DAILY_TOUCH_NOTE")
    path = write_marker(msg)
    res = git_commit_and_push(path)
    print("Daily touch result:", res)


if __name__ == "__main__":
    main()
