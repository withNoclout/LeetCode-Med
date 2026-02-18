class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Alice can always choose to leave just the first element or just the last element
        # in her very first move.
        # Any attempt to play for a better "internal" element allows Bob (who plays next)
        # to force the result to be min(new_start, new_end).
        # Bob can always cap the result at the boundary values. 
        # Since Alice wants to maximize, she should simply take the best boundary 
        # available to her immediately.
        
        return max(nums[0], nums[-1])
