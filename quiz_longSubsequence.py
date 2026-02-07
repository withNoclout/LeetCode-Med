class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor_sum = 0
        has_non_zero = False
        
        for x in nums:
            xor_sum ^= x
            if x != 0:
                has_non_zero = True
                
        # Case 1: All elements are 0, so no subsequence can have non-zero XOR
        if not has_non_zero:
            return 0
            
        # Case 2: The XOR of the entire array is already non-zero
        if xor_sum != 0:
            return n
            
        # Case 3: Total XOR is 0.
        # Since there is at least one non-zero element 'x', removing it 
        # changes the XOR sum to (0 ^ x) = x, which is non-zero.
        # Thus, we can achieve the goal by removing just 1 element.
        return n - 1
