class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [[0] * 101 for _ in range(n + 1)]
        for i in range(n):
            for v in range(1, 101):
                prefix[i + 1][v] = prefix[i][v]
            prefix[i + 1][nums[i]] += 1

        res = []
        for l, r in queries:
            prev = -1
            mindiff = float('inf')
            for v in range(1, 101):
                if prefix[r + 1][v] - prefix[l][v] > 0:
                    if prev != -1:
                        mindiff = min(mindiff, v - prev)
                    prev = v
            res.append(-1 if mindiff == float('inf') else mindiff)
        return res
