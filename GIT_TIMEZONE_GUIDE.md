# Git Timezone Guide

## Understanding Git Commit Timestamps

Git records two timestamps for each commit:
- **Author Date**: When the changes were originally made
- **Committer Date**: When the commit was applied to the repository

Both timestamps include timezone information.

## Why Commits Show Up on Different Days

If you commit code before midnight in your local timezone but it shows up on the next day in the git log, this is likely due to timezone differences:

1. **Git uses UTC by default** in many contexts
2. **GitHub displays times in UTC** by default
3. **Your local timezone** may be ahead of or behind UTC

### Example:
- You commit at **11:30 PM PST** (UTC-8)
- Git records the time as **7:30 AM UTC** (next day)
- GitHub shows the commit on the **next day** because it uses UTC

## Solutions

### Option 1: Configure Git to Use Your Local Timezone

Set your timezone in git config:

```bash
# Set your timezone (e.g., America/Los_Angeles for PST/PDT)
git config --global log.date local

# Or specify a timezone for display
export TZ='America/Los_Angeles'  # Add to your ~/.bashrc or ~/.zshrc
```

### Option 2: View Commits in Your Local Timezone

Use git log with local date format:

```bash
# Show commits with local timezone
git log --date=local

# Show commits with relative time
git log --date=relative

# Show commits with ISO format including timezone
git log --date=iso-local
```

### Option 3: Set Timezone Before Committing

Before making commits, set your timezone:

```bash
# Linux/Mac
export TZ='America/New_York'
git commit -m "Your message"

# Windows (PowerShell)
$env:TZ='America/New_York'
git commit -m "Your message"
```

## Common Timezones

- **PST/PDT**: America/Los_Angeles (UTC-8/-7)
- **EST/EDT**: America/New_York (UTC-5/-4)
- **CST/CDT**: America/Chicago (UTC-6/-5)
- **MST/MDT**: America/Denver (UTC-7/-6)
- **UTC**: Etc/UTC (UTC+0)
- **GMT**: Europe/London (UTC+0/+1)
- **CET/CEST**: Europe/Paris (UTC+1/+2)
- **IST**: Asia/Kolkata (UTC+5:30)
- **JST**: Asia/Tokyo (UTC+9)
- **AEST/AEDT**: Australia/Sydney (UTC+10/+11)

## Checking Your Current Settings

```bash
# Check git date format configuration
git config --get log.date

# Check system timezone
echo $TZ

# View a commit with all timezone information
git show --format=fuller <commit-hash>
```

## Helper Script

Use the included `git-timezone-helper.sh` script to view commits in different timezones:

```bash
./git-timezone-helper.sh
```

## Important Notes

1. **Changing timezone settings doesn't change commit timestamps** - it only changes how they are displayed
2. **GitHub always displays times in your browser's timezone** when you're logged in
3. **The actual commit timestamp is always stored with full timezone information** and never changes
4. **Timezone in commits is determined by your system's TZ environment variable** at commit time

## Recommended Configuration

Add to your `~/.gitconfig`:

```ini
[log]
    date = iso-local  # Shows timezone info clearly

[alias]
    # Alias to show commits in local time
    llog = log --date=local
    # Alias to show commits with full timezone info
    logtz = log --format='%h %ai %s'
```

## References

- [Git Documentation - Date Formats](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dateltformatgt)
- [Understanding Timezones in Git](https://stackoverflow.com/questions/7853332/how-to-change-the-timezone-of-a-git-commit)
