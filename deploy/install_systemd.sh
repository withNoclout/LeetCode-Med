#!/usr/bin/env bash
set -euo pipefail

# Install systemd unit and timer (requires sudo)
# Usage: sudo ./deploy/install_systemd.sh

SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="${SRC_DIR%/deploy}"

echo "Installing systemd unit and timer for checker..."

sudo cp "${SRC_DIR}/systemd/checker.service" /etc/systemd/system/
sudo cp "${SRC_DIR}/systemd/checker.timer" /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable --now checker.timer

echo "Enabled checker.timer. Check status with: sudo systemctl status checker.timer" 
