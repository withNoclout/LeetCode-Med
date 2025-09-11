class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        res = s = 0
        for num in nums:
            s += num
            res += count[s - goal]
            count[s] += 1
        return res
