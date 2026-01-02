# Deploying the checker as a scheduled job

This folder contains sample artifacts to run `checker/checker.py` every 12 hours.

Options:

- systemd timer (recommended on modern Linux):
  - Copy `deploy/systemd/checker.service` and `deploy/systemd/checker.timer` to `/etc/systemd/system`.
  - Or run the installer (requires sudo):

```bash
sudo deploy/install_systemd.sh
```

  - Check status:

```bash
sudo systemctl status checker.timer
sudo journalctl -u checker.service -f
```

- user-level systemd: copy the two files to `~/.config/systemd/user/` and run:

```bash
systemctl --user daemon-reload
systemctl --user enable --now checker.timer
```

- cron (alternative):
  - Add the line from `deploy/cron_entry.txt` to your crontab (`crontab -e`).
  - Make sure the path to Python and working dir match your environment.

Daily commits / activity
------------------------

If you want a daily guaranteed commit (a small marker file is created in `checked/daily_edits/`):

 - The repository contains `deploy/daily/daily_touch.py` which writes `checked/daily_edits/YYYY-MM-DD.md` and commits & pushes it.
 - A systemd timer `deploy/systemd/daily-touch.timer` and service are provided to run this script daily at 00:05 UTC.
 - Install with the same `deploy/install_systemd.sh` or copy the unit and timer into `/etc/systemd/system` and enable them:

```bash
sudo cp deploy/systemd/daily-touch.service /etc/systemd/system/
sudo cp deploy/systemd/daily-touch.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now daily-touch.timer
```

 - If you prefer cron, add a line like below to `crontab -e`:

```
5 0 * * * cd /home/noclout/LeetCode-Med && /usr/bin/python3 deploy/daily/daily_touch.py >> /var/log/leetcode_daily.log 2>&1
```


Secrets / environment:

- The checker reads `DEEPSEEK_URL` and `DEEPSEEK_API_KEY` from the environment. Do NOT commit secrets.
- Copy `checker/.env.example` to `checker/.env` (gitignored) and set values, or set environment variables in the systemd unit or cron wrapper.

Example systemd override to set env (create `/etc/systemd/system/checker.service.d/override.conf`):

```
[Service]
Environment=DEEPSEEK_URL=https://api.deepseek.example/verify
Environment=DEEPSEEK_API_KEY=sk-xxxxx
```
