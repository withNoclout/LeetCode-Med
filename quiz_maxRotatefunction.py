class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums ) 
        total_sum = sum(nums) 
        f=  sum(i * num for i, num in enumerate(nums))
        res = f 
        for k in range(1 , n ) : 
            f += total_sum - n * nums[n - k]
            res = max(res, f)
        return res
