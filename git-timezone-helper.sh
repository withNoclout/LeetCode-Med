#!/bin/bash

# Git Timezone Helper Script
# This script helps you view git commits in different timezones

echo "========================================"
echo "Git Timezone Helper"
echo "========================================"
echo ""

# Show current system timezone
echo "Current System Timezone:"
if [ -n "$TZ" ]; then
    echo "  TZ environment variable: $TZ"
else
    echo "  TZ environment variable: Not set (using system default)"
fi
echo "  Date command output: $(date)"
echo ""

# Show last 10 commits in different formats
echo "Last 10 Commits (Different Timezone Formats):"
echo ""

echo "--- Default Format (usually UTC or your git config) ---"
git log -10 --oneline --format='%h %ad %s' 2>/dev/null || echo "No commits found"
echo ""

echo "--- ISO Format with Timezone ---"
git log -10 --date=iso --format='%h %ad %s' 2>/dev/null || echo "No commits found"
echo ""

echo "--- Local Timezone ---"
git log -10 --date=local --format='%h %ad %s' 2>/dev/null || echo "No commits found"
echo ""

echo "--- Relative Time ---"
git log -10 --date=relative --format='%h %ad %s' 2>/dev/null || echo "No commits found"
echo ""

echo "--- Raw Timestamp (Unix epoch + timezone) ---"
git log -10 --date=raw --format='%h %ad %s' 2>/dev/null || echo "No commits found"
echo ""

echo "========================================"
echo "Timezone Conversion Examples:"
echo "========================================"
echo ""

# Get the latest commit timestamp
latest_commit=$(git log -1 --format='%at' 2>/dev/null)

if [ -n "$latest_commit" ]; then
    echo "Latest commit timestamp: $latest_commit (Unix epoch)"
    echo ""
    
    # Common timezones
    timezones=(
        "UTC"
        "America/New_York"
        "America/Chicago"
        "America/Denver"
        "America/Los_Angeles"
        "Europe/London"
        "Europe/Paris"
        "Asia/Tokyo"
        "Asia/Kolkata"
        "Australia/Sydney"
    )
    
    echo "Same commit in different timezones:"
    for tz in "${timezones[@]}"; do
        formatted_date=$(TZ="$tz" date -d "@$latest_commit" "+%Y-%m-%d %H:%M:%S %Z" 2>/dev/null)
        if [ $? -eq 0 ]; then
            printf "  %-25s %s\n" "$tz:" "$formatted_date"
        fi
    done
else
    echo "No commits found in this repository"
fi

echo ""
echo "========================================"
echo "How to Use Different Timezones:"
echo "========================================"
echo ""
echo "1. View logs in local timezone:"
echo "   git log --date=local"
echo ""
echo "2. Set timezone for a single command:"
echo "   TZ='America/New_York' git log"
echo ""
echo "3. Set timezone permanently (add to ~/.bashrc or ~/.zshrc):"
echo "   export TZ='America/Los_Angeles'"
echo ""
echo "4. Configure git to always use local date:"
echo "   git config --global log.date local"
echo ""
echo "5. View commit with full timezone information:"
echo "   git show --format=fuller HEAD"
echo ""
