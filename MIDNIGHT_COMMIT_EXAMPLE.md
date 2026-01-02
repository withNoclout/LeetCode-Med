# Real-World Example: Why Your Midnight Commits Show Up on the Wrong Day

## The Scenario

You're in **Los Angeles (PST, UTC-8)** and you commit code at **11:30 PM on January 1st**.

```bash
# Your local time: January 1, 2026, 11:30 PM PST
git commit -m "Last minute fix before deadline"
```

## What Git Records

Git stores the commit with **UTC timezone**:
```
Author Date: January 2, 2026, 7:30 AM UTC
Commit Date: January 2, 2026, 7:30 AM UTC
```

## What You See

### On GitHub (default view)
- Shows: **January 2, 2026**
- Reason: GitHub displays in UTC or your browser's timezone

### In `git log` (default)
- Shows: **January 2, 2026**
- Reason: Git defaults to showing commit times in UTC

### In `git log --date=local`
- Shows: **January 1, 2026, 11:30 PM**
- Reason: Git converts UTC back to your local timezone

## Visual Timeline

```
Your Local Time (PST, UTC-8):
Jan 1 ─────────────────────────────── 11:30 PM ───┐
                                                   │ You commit here
                                                   │
UTC (What Git stores):                             │
Jan 2 ──────── 7:30 AM ────────────────────────────┘
               └─ This is what GitHub shows!

When midnight passes in PST:
Jan 2 ───── 12:00 AM ── 12:01 AM ── ... (PST)
               │
               │
Jan 2 ───── 8:00 AM ─── 8:01 AM ── ... (UTC)
            └─ Your 11:30 PM PST commit was already at 7:30 AM UTC!
```

## Common Timezones and Their Offset

When you commit at **11:30 PM local time**, here's what time it is in UTC:

| Timezone | Local Time | UTC Time (Next Day!) |
|----------|------------|---------------------|
| PST (UTC-8) | Jan 1, 11:30 PM | Jan 2, 7:30 AM |
| MST (UTC-7) | Jan 1, 11:30 PM | Jan 2, 6:30 AM |
| CST (UTC-6) | Jan 1, 11:30 PM | Jan 2, 5:30 AM |
| EST (UTC-5) | Jan 1, 11:30 PM | Jan 2, 4:30 AM |

**Only commits after 4:00 PM PST will show up on the SAME day in UTC!**

## The Fix

### Option 1: Just Accept It
The timestamp is correct - it's just displayed in a different timezone. Your commit still has the right time encoded.

### Option 2: View in Local Time
```bash
git config --global log.date local
git log
```

### Option 3: Use Relative Time
```bash
git log --date=relative
# Shows: "2 hours ago" instead of specific dates
```

## Important Realizations

1. **The timestamp is CORRECT** - it's just in UTC
2. **GitHub knows your timezone** - when logged in, it should show your local time
3. **The "day" is relative** - it depends on which timezone you're looking at
4. **This is not a bug** - it's how Git is designed to work globally

## Pro Tip

If you're trying to maintain a daily commit streak and your timezone causes confusion, commit before:
- **4:00 PM PST** (to show on the same day in UTC)
- Or just don't worry about it - GitHub's contribution graph uses your local timezone when you're logged in!
