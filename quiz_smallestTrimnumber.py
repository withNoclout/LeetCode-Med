class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        m = len(nums[0])
        n = len(nums)
        order = {}

        for t in range(1, m + 1):
            arr = []
            for i in range(n):
                arr.append((nums[i][-t:], i))
            arr.sort()
            order[t] = [idx for _, idx in arr]

        res = []
        for k, trim in queries:
            res.append(order[trim][k - 1])
        return res
