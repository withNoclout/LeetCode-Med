class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums) % p
        if total == 0:
            return 0
        prefix = 0
        seen = {0: -1}
        res = len(nums)
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - total) % p
            if target in seen:
                res = min(res, i - seen[target])
            seen[prefix] = i
        return res if res < len(nums) else -1
