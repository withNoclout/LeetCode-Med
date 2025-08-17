class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        
        curr = 0
        total = 0
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                total += curr
            else:
                curr = 0
        
        return total
