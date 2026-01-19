class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The problem requires the final array to be non-decreasing.
        # Since we can only "merge" subarrays into their maximum value, 
        # we cannot eliminate a large number to reveal a smaller number after it.
        # We can only keep a number if it is >= the current maximum we've decided to keep.
        
        count = 0
        current_max = 0  # Constraints say nums[i] >= 1, so 0 is a safe start
        
        for num in nums:
            if num >= current_max:
                # If the current number maintains the non-decreasing order, keep it.
                count += 1
                current_max = num
            # Else: num < current_max
            # This number must be merged into the previous maximum (current_max)
            # to maintain the property, effectively deleting it from the count.
                
        return count
