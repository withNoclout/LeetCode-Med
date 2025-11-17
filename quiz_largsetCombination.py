class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        ans = 0
        for bit in range(24, -1, -1):
            cnt = 0
            mask = 1 << bit
            for x in candidates:
                if x & mask:
                    cnt += 1
            ans = max(ans, cnt)
        return ans
