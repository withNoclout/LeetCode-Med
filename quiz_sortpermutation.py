class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize ans with -1 (all 1s in binary) to act as the identity for Bitwise AND
        ans = -1
        has_misplaced = False
        
        for i, x in enumerate(nums):
            # If element x is not at its sorted position i
            if x != i:
                ans &= x
                has_misplaced = True
        
        # If the array is already sorted, the problem specifies returning 0
        if not has_misplaced:
            return 0
            
        return an
