class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # memo[r][c] stores the length of the longest increasing path starting at (r, c)
        memo = [[0] * cols for _ in range(rows)]
        
        def dfs(r, c):
            # If we've already calculated the path for this cell, return it
            if memo[r][c] != 0:
                return memo[r][c]
            
            max_path = 1 # Every cell is a path of length 1
            
            # Explore 4 directions: up, down, left, right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and the "strictly increasing" condition
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            # Save result in memo before returning
            memo[r][c] = max_path
            return max_path
        
        # Start DFS from every single cell in the matrix
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
                
        return res
