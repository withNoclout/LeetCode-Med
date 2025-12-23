import sys

# Essential: Increase recursion depth for deep trees (N=2000)
sys.setrecursionlimit(3000)

class Solution(object):
    def maxOperations(self, nums):
        n = len(nums)
        
        def solve(l, r, target):
            # Optimization: Use a 2D array (List of Lists) instead of a dictionary.
            # -1 represents an uncomputed state.
            memo = [[-1] * n for _ in range(n)]
            
            def dfs(i, j):
                # Base case: Not enough elements left
                if i >= j: 
                    return 0
                
                # Check memoization table
                if memo[i][j] != -1: 
                    return memo[i][j]
                
                res = 0
                # Option 1: Remove first two
                if nums[i] + nums[i+1] == target:
                    res = max(res, 1 + dfs(i+2, j))
                    
                # Option 2: Remove first and last
                if nums[i] + nums[j] == target:
                    res = max(res, 1 + dfs(i+1, j-1))
                    
                # Option 3: Remove last two
                if nums[j] + nums[j-1] == target:
                    res = max(res, 1 + dfs(i, j-2))
                
                # Store result in table
                memo[i][j] = res
                return res
            
            return dfs(l, r)

        res = 0
        # Case 1: Start by removing first two
        res = max(res, 1 + solve(2, n-1, nums[0] + nums[1]))
        
        # Case 2: Start by removing first and last
        res = max(res, 1 + solve(1, n-2, nums[0] + nums[-1]))
        
        # Case 3: Start by removing last two
        res = max(res, 1 + solve(0, n-3, nums[-2] + nums[-1]))
        
        return res
