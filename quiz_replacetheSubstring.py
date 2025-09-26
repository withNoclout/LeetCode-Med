class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        n = len(s)
        count = Counter(s)
        required = n // 4
        if all(count[c] == required for c in "QWER"):
            return 0

        res = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[c] <= required for c in "QWER"):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res
