class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            cnt = [0] * 26
            maxf = 0
            for j in range(i, n):
                idx = ord(s[j]) - 97
                cnt[idx] += 1
                if cnt[idx] > maxf:
                    maxf = cnt[idx]
                minf = float('inf')
                for c in cnt:
                    if c > 0 and c < minf:
                        minf = c
                res += maxf - minf
        return res
