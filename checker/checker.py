#!/usr/bin/env python3
"""
Checker service: pick one Quiz_*.py file and validate it, then move to `checked/`.

Usage:
  - Run once: `python checker.py`
  - Run as daemon: `python checker.py --daemon` (checks one file every 12 hours)

Validation:
  - Uses local validation function (no external APIs required)
  - Checks filename format, Solution class structure, method naming conventions
  - Validates code syntax and structure

The script will create/maintain `checker/state.json` and `checked/metadata.json`.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
import re
import ast

ROOT = Path(__file__).resolve().parents[1]
CHECKED_DIR = ROOT / "checked"
STATE_FILE = Path(__file__).resolve().parents[0] / "state.json"
METADATA_FILE = CHECKED_DIR / "metadata.json"
ENV_FILE = Path(__file__).resolve().parents[0] / ".env"
INTERVAL_HOURS = 12


def load_env():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"next_index": 0, "files": {}}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def list_quiz_files():
    # match files starting with Quiz_ or quiz_ (older ones)
    files = [p for p in ROOT.glob("Quiz_*.py")] + [p for p in ROOT.glob("quiz_*.py")]
    # exclude files already in checked directory
    files = [p for p in files if CHECKED_DIR not in p.parents]
    files = sorted(files, key=lambda p: p.name)
    return files


def parse_solution_methods(path: Path):
    src = path.read_text()
    try:
        tree = ast.parse(src)
    except Exception:
        return []
    methods = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods.append(item.name)
    return methods


def filename_function_fragment(name: str) -> str:
    # Quiz_01_lasttimeCachBus.py -> lasttimeCachBus
    m = re.match(r"Quiz_\d+_(.+)\.py", name, re.IGNORECASE)
    if not m:
        m = re.match(r"quiz_(.+)\.py", name, re.IGNORECASE)
    return m.group(1) if m else ""


def check_name_vs_methods(filename: str, methods: list[str]) -> bool:
    frag = filename_function_fragment(filename).lower()
    if not frag:
        return False
    frag_parts = re.split(r"[_\-]+", frag)
    frag_words = set()
    for part in frag_parts:
        # split camelCase
        frag_words.update(re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", part))
        frag_words.add(part)
    frag_words = {w.lower() for w in frag_words if w}
    for m in methods:
        words = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", m)
        words = {w.lower() for w in words}
        # if there's overlap of meaningful words, assume a match
        if frag_words & words:
            return True
    return False


def validate_solution_local(filename: str, content: str) -> dict:
    """
    Local validation function that checks LeetCode solutions without external APIs.
    Validates:
    - Filename format (Quiz_XX_funcname.py)
    - Solution class exists
    - Method names match filename conventions
    - Code structure and syntax
    """
    result = {
        "filename_valid": False,
        "has_solution_class": False,
        "method_names_match": False,
        "has_docstrings": False,
        "has_type_hints": False,
        "code_length_ok": False,
        "issues": []
    }
    
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        result["issues"].append(f"Syntax Error: {str(e)}")
        return result
    
    # Check filename format
    if re.match(r"Quiz_\d+_.+\.py", filename, re.IGNORECASE) or re.match(r"quiz_.+\.py", filename, re.IGNORECASE):
        result["filename_valid"] = True
    else:
        result["issues"].append(f"Invalid filename format: {filename}")
    
    # Check for Solution class
    solution_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            solution_class = node
            result["has_solution_class"] = True
            break
    
    if not solution_class:
        result["issues"].append("No 'Solution' class found")
        return result
    
    # Get methods from Solution class
    methods = []
    for item in solution_class.body:
        if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
            methods.append(item.name)
            # Check for docstring
            if ast.get_docstring(item):
                result["has_docstrings"] = True
            # Check for type hints
            if item.returns or any(arg.annotation for arg in item.args.args):
                result["has_type_hints"] = True
    
    # Check if method names match filename
    if check_name_vs_methods(filename, methods):
        result["method_names_match"] = True
    else:
        result["issues"].append(f"Method names don't match filename. Methods: {methods}")
    
    # Check code length (should not be too short or too long for typical LeetCode)
    lines = content.count('\n')
    if 5 < lines < 500:  # Reasonable bounds for LeetCode solution
        result["code_length_ok"] = True
    else:
        result["issues"].append(f"Code length unusual: {lines} lines")
    
    return result


def commit_and_push(files: list[Path], message: str) -> dict:
    try:
        subprocess.check_call(["git", "add"] + [str(p) for p in files])
        subprocess.check_call(["git", "commit", "-m", message])
        # attempt push to origin current branch
        subprocess.check_call(["git", "push", "origin", "HEAD"])
        return {"ok": True}
    except subprocess.CalledProcessError as e:
        return {"ok": False, "error": str(e)}


def perform_check(run_once=True):
    files = list_quiz_files()
    if not files:
        print("No quiz files found.")
        return

    state = load_state()
    idx = state.get("next_index", 0) % len(files)

    # try to find a file not checked in the last INTERVAL_HOURS
    chosen = None
    now = datetime.utcnow()
    for i in range(len(files)):
        candidate = files[(idx + i) % len(files)]
        meta = state.get("files", {}).get(str(candidate.name), {})
        last = meta.get("last_checked")
        if not last:
            chosen = candidate
            idx = (idx + i) % len(files)
            break
        last_dt = datetime.fromisoformat(last)
        if now - last_dt >= timedelta(hours=INTERVAL_HOURS):
            chosen = candidate
            idx = (idx + i) % len(files)
            break

    if chosen is None:
        # fallback to next index
        chosen = files[idx]

    print(f"Checking {chosen}")
    methods = parse_solution_methods(chosen)
    name_ok = check_name_vs_methods(chosen.name, methods)
    content = chosen.read_text()

    # Use local validation instead of external API
    validation_result = validate_solution_local(chosen.name, content)

    # Determine if file should be moved (only if validation passed)
    is_valid = (
        validation_result.get("filename_valid", False) and
        validation_result.get("has_solution_class", False) and
        validation_result.get("code_length_ok", False) and
        name_ok and
        len(validation_result.get("issues", [])) == 0
    )

    if is_valid:
        # prepare checked dir
        CHECKED_DIR.mkdir(exist_ok=True)
        dest = CHECKED_DIR / chosen.name
        shutil.move(str(chosen), str(dest))
        
        # record metadata
        METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        metadata = METADATA_FILE.exists() and json.loads(METADATA_FILE.read_text()) or []
        entry = {
            "original": str(chosen.name),
            "moved_to": str(dest.relative_to(ROOT)),
            "checked_at": now.isoformat(),
            "methods": methods,
            "name_ok": name_ok,
            "validation": validation_result,
            "status": "PASSED"
        }
        metadata.insert(0, entry)
        METADATA_FILE.write_text(json.dumps(metadata, indent=2))

        # update state
        state.setdefault("files", {})[chosen.name] = {"last_checked": now.isoformat()}
        state["next_index"] = (idx + 1) % len(files)
        save_state(state)

        # commit changes
        commit_msg = f"checker: validated {chosen.name} (PASSED)"
        commit_res = commit_and_push([METADATA_FILE, STATE_FILE, dest], commit_msg)
        print(f"✓ PASSED - File moved to checked/")
        print("Commit result:", commit_res)
    else:
        # File failed validation - skip it, don't move
        print(f"✗ FAILED - File skipped (not moved)")
        print(f"  Issues: {validation_result.get('issues', [])}")
        
        # Still update state to mark as checked but failed
        state.setdefault("files", {})[chosen.name] = {
            "last_checked": now.isoformat(),
            "status": "FAILED",
            "issues": validation_result.get("issues", [])
        }
        state["next_index"] = (idx + 1) % len(files)
        save_state(state)
        print(f"  (Will retry this file in {INTERVAL_HOURS} hours)")


def main():
    load_env()
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", action="store_true", help="Run continuously, sleeping 12 hours between checks")
    args = parser.parse_args()

    if args.daemon:
        while True:
            perform_check(run_once=False)
            time.sleep(INTERVAL_HOURS * 3600)
    else:
        perform_check(run_once=True)


if __name__ == "__main__":
    main()
