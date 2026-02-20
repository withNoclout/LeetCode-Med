class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Place each valid number in its correct position
        for i in range(n):
            # While the number is in the range [1, n] and not at its correct index
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the number to its correct index (nums[i] - 1)
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first index that doesn't have the correct number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If all numbers 1 to n are present, the missing one is n + 1
        return n + 1
