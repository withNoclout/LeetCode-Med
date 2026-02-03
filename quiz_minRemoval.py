class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Sort the array to easily identify min and max in a window
        nums.sort()
        
        n = len(nums)
        left = 0
        max_balanced_len = 0
        
        # Step 2: Sliding Window
        # We want the longest window [left, right] such that nums[right] <= nums[left] * k
        for right in range(n):
            # If the condition is violated (current max > current min * k), shrink the window from the left
            while nums[right] > nums[left] * k:
                left += 1
            
            # Update the maximum length of a valid balanced window found so far
            max_balanced_len = max(max_balanced_len, right - left + 1)
            
        # Step 3: The minimum removals is Total Elements - Max Keepable Elements
        return n - max_balanced_len
