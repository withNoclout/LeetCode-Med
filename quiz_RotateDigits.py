from functools import lru_cache

class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        valid = {0,1,2,5,6,8,9}
        diffset = {2,5,6,9}

        @lru_cache(None)
        def dfs(i, tight, diff):
            if i == len(s):
                return 1 if diff else 0
            limit = int(s[i]) if tight else 9
            res = 0
            for d in range(0, limit + 1):
                if d not in valid:
                    continue
                res += dfs(i + 1, tight and d == limit, diff or (d in diffset))
            return res

        return dfs(0, True, False)
