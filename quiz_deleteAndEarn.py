from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = Counter(nums)
        nums_sorted = sorted(count.keys())
        n = len(nums_sorted)
        
        take, skip = 0, 0
        prev = None
        for x in nums_sorted:
            earn = x * count[x]
            if prev is not None and x == prev + 1:
                take, skip = skip + earn, max(skip, take)
            else:
                take, skip = max(take, skip) + earn, max(take, skip)
            prev = x
        return max(take, skip)
