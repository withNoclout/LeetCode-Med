class Solution(object):
    def maxOperations(self, nums):
        n = len(nums)
        
        def solve(l, r, target):
            memo = {}
            def dp(i, j):
                if i >= j: return 0
                if (i, j) in memo: return memo[(i, j)]
                
                res = 0
                # Option 1: Remove first two
                if nums[i] + nums[i+1] == target:
                    res = max(res, 1 + dp(i+2, j))
                # Option 2: Remove first and last
                if nums[i] + nums[j] == target:
                    res = max(res, 1 + dp(i+1, j-1))
                # Option 3: Remove last two
                if nums[j-1] + nums[j] == target:
                    res = max(res, 1 + dp(i, j-2))
                
                memo[(i, j)] = res
                return res
            return dp(l, r)

        res = 0
        # Case 1: Start by removing first two
        res = max(res, 1 + solve(2, n-1, nums[0] + nums[1]))
        # Case 2: Start by removing first and last
        res = max(res, 1 + solve(1, n-2, nums[0] + nums[-1]))
        # Case 3: Start by removing last two
        res = max(res, 1 + solve(0, n-3, nums[-2] + nums[-1]))
        
        return res
