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

Secrets / environment:

- The checker reads `DEEPSEEK_URL` and `DEEPSEEK_API_KEY` from the environment. Do NOT commit secrets.
- Copy `checker/.env.example` to `checker/.env` (gitignored) and set values, or set environment variables in the systemd unit or cron wrapper.

Example systemd override to set env (create `/etc/systemd/system/checker.service.d/override.conf`):

```
[Service]
Environment=DEEPSEEK_URL=https://api.deepseek.example/verify
Environment=DEEPSEEK_API_KEY=sk-xxxxx
```
