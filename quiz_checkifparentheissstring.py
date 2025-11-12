class Solution(object):
    def canBeValid(self, s, locked):
        n = len(s)
        if n % 2:  # odd length can never be balanced
            return False

        # Left-to-right: ensure we can avoid having too many ')'
        cnt = 0
        for i in range(n):
            if locked[i] == '1':
                cnt += 1 if s[i] == '(' else -1
            else:
                cnt += 1  # treat unlocked as '('
            if cnt < 0:
                return False

        # Right-to-left: ensure we can avoid having too many '('
        cnt = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                cnt += 1 if s[i] == ')' else -1
            else:
                cnt += 1  # treat unlocked as ')'
            if cnt < 0:
                return False

        return True
