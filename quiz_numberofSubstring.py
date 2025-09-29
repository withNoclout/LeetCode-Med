class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        res, left = 0, 0

        for right in range(n):
            count[s[right]] += 1
            # shrink left until substring no longer has all 3 chars
            while all(count[c] > 0 for c in "abc"):
                res += n - right
                count[s[left]] -= 1
                left += 1

        return res
