class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Collect all elements in the k x k submatrix
                nums = []
                for r in range(i, i + k):
                    nums.extend(grid[r][j:j+k])
                
                nums.sort()
                
                # Find min diff between distinct adjacent elements
                min_d = float('inf')
                for x in range(1, len(nums)):
                    if nums[x] != nums[x-1]:
                        d = nums[x] - nums[x-1]
                        if d < min_d:
                            min_d = d
                
                # If min_d is still inf, it means all elements were identical
                ans[i][j] = min_d if min_d != float('inf') else 0
                
        return ans
