class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # If nums is empty, technically they are "equal".
        if not nums:
            return True
            
        # If k is 0, we cannot change values. They must already be equal.
        if k == 0:
            return len(set(nums)) == 1
            
        # Standard case: All numbers must be congruent modulo k.
        # This implies |nums[i] - nums[j]| is a multiple of k.
        remainder = nums[0] % k
        
        for x in nums:
            if x % k != remainder:
                return False
                
        return True
