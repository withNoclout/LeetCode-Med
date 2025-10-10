class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        # left[i][j]: length of equal suffix ending at s[i-1], t[j-1]
        left = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            si = s[i-1]
            row = left[i]
            prev_row = left[i-1]
            for j in range(1, n+1):
                if si == t[j-1]:
                    row[j] = prev_row[j-1] + 1

        # right[i][j]: length of equal prefix starting at s[i], t[j]
        right = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            si = s[i]
            row = right[i]
            next_row = right[i+1]
            for j in range(n-1, -1, -1):
                if si == t[j]:
                    row[j] = next_row[j+1] + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    ans += (left[i][j] + 1) * (right[i+1][j+1] + 1)
        return ans

