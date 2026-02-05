class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Convert to absolute values and sort
        # Logic: The condition min(|a-b|, |a+b|) <= min(|a|, |b|) simplifies to:
        # For |a| <= |b|, we need |b| <= 2 * |a|
        arr = sorted([abs(x) for x in nums])
        
        n = len(arr)
        ans = 0
        left = 0
        
        # Step 2: Sliding Window / Two Pointers
        for right in range(n):
            # We need arr[left] * 2 >= arr[right] (where arr[left] is the smaller value)
            # If the smallest value in the window is too small, shrink from the left
            while left < right and arr[left] * 2 < arr[right]:
                left += 1
            
            # All indices from 'left' to 'right-1' form a valid pair with 'right'
            ans += (right - left)
            
        return ans
