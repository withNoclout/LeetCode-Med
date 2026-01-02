# Git Timezone Quick Reference

## The Problem
Commits made before midnight in your timezone appear on the next day in GitHub/git log.

## Why This Happens
- Git records timestamps in UTC by default
- Your local time might be behind UTC
- Example: 11:30 PM PST (UTC-8) = 7:30 AM UTC next day

## Quick Solutions

### 1. View Commits in Your Timezone
```bash
git log --date=local
```

### 2. Configure Git to Always Use Local Time
```bash
git config --global log.date local
```

### 3. Set Your System Timezone
```bash
# Linux/Mac (add to ~/.bashrc or ~/.zshrc)
export TZ='America/Los_Angeles'

# Windows PowerShell (add to profile)
$env:TZ='America/New_York'
```

### 4. View Specific Commit with Full Details
```bash
git show --format=fuller HEAD
```

## Useful Git Aliases

Add these to your `~/.gitconfig`:
```ini
[alias]
    llog = log --date=local
    today = log --since='midnight' --date=local
```

Then use:
```bash
git llog        # View logs in local time
git today       # See today's commits
```

## Check Your Settings
```bash
# See how git will display dates
git config --get log.date

# See current timezone
echo $TZ

# Run the helper script
./git-timezone-helper.sh
```

## Important Notes
- [YES] Changing display settings only affects how times are SHOWN
- [YES] The actual commit timestamp never changes
- [YES] All timezone information is preserved in commits
- [NO] You cannot "fix" old commit timestamps without rewriting history

## Need More Help?
See [GIT_TIMEZONE_GUIDE.md](GIT_TIMEZONE_GUIDE.md) for detailed information.
