# LeetCode-Med (small updates)

This repo contains small LeetCode solutions. Changes added:

- `numofWays_2417.py`: cleaned-up module for the problem implementation.
- `tests/test_numofWays.py`: simple unit tests for the `numberOfWays` method.

Run tests:

```bash
python -m unittest discover -v
```

## Git Timezone Information

If you're experiencing issues where commits made before midnight appear on the next day, this is due to timezone differences between your local time and UTC (the default timezone Git uses).

**Quick Fix:**
```bash
# Configure git to display times in your local timezone
git config --global log.date local
```

**For more information:**
- See [GIT_TIMEZONE_GUIDE.md](GIT_TIMEZONE_GUIDE.md) for detailed explanations
- Run `./git-timezone-helper.sh` to view your commits in different timezones
