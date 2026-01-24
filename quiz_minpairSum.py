class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_pair_sum = 0
        
        # Pair the smallest with the largest, second smallest with second largest, etc.
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            max_pair_sum = max(max_pair_sum, current_sum)
            
        return max_pair_sum
