# LeetCode-Med AI Coding Instructions

## Project Overview
This repository is a collection of LeetCode solutions (primarily Python) with an automated organization and activity system.

## File Naming Conventions
- **New Solutions:** Use the format `Quiz_{number}_{FunctionName}.py` (e.g., `Quiz_03_mySolution.py`).
- **Legacy Files:** Files named `quiz_*.py` are legacy and are being phased out by the automated checker.
- **Processed Files:** Once validated, files are moved to the `checked/` directory.

## Automated Services
- **Checker Service (`checker/checker.py`):** Runs every 12 hours via `checker.timer`. It validates one file at a time, calls the DeepSeek API for analysis, and moves it to `checked/`.
- **Daily Touch (`deploy/daily/daily_touch.py`):** Runs daily at 00:05 UTC via `daily-touch.timer`. It creates a dated marker in `checked/daily_edits/` to ensure daily GitHub activity.

## Coding Guidelines
1. **LeetCode Format:** Always use the standard LeetCode `Solution` class structure.
2. **Safety First:** If a change might impact the backend/automation services, stop the services before implementing:
   ```bash
   sudo systemctl stop checker.timer daily-touch.timer
   ```
   Restart them after completion:
   ```bash
   sudo systemctl start checker.timer daily-touch.timer
   ```
3. **Documentation:** Read any documentation in the `docs/` folder (if present) before implementing new features.
4. **Dependencies:** Use `requests` for API calls. Avoid adding heavy dependencies unless necessary.

## Deployment & Workflows
- **Systemd Timers:** Services are managed via systemd. Use `systemctl list-timers` to check schedules.
- **Git Workflow:** The automated services commit and push directly to `origin/main`. Always pull before making manual changes to avoid conflicts.
- **Secrets:** Never commit `.env` files. Use `checker/.env` for local secrets (gitignored).
