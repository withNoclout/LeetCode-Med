class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        total = sum(nums)
        
        # 1. Validation: The total sum must be divisible by the target sum.
        if target == 0 or total % target != 0:
            return False
            
        # k is the number of subsets we need to form
        k = total // target
        n = len(nums)
        
        # Sort in descending order to optimize backtracking (try larger elements first)
        nums.sort(reverse=True)
        
        # If the largest element is already greater than target, impossible
        if nums[0] > target:
            return False
            
        used = [False] * n
        
        def backtrack(start_index, k_left, current_sum):
            # Base Case: We have formed all required subsets
            if k_left == 0:
                return True
            
            # If current subset is complete, start forming the next one
            if current_sum == target:
                return backtrack(0, k_left - 1, 0)
            
            for i in range(start_index, n):
                if not used[i]:
                    # Optimization: Skip duplicates to avoid redundant work
                    if i > start_index and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                        
                    if current_sum + nums[i] <= target:
                        used[i] = True
                        if backtrack(i + 1, k_left, current_sum + nums[i]):
                            return True
                        used[i] = False
                        
                        # Optimization: If we failed to fill the bucket starting with an empty sum
                        # or if we couldn't complete it with the current element, no other combination will work.
                        if current_sum == 0:
                            return False
                            
            return False

        # Start backtracking: index 0, need k subsets, current bucket sum 0
        return backtrack(0, k, 0)
