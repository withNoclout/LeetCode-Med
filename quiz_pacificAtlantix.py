class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prevHeight):
            # out of bounds / already visited / downhill -> stop
            if (r, c) in visited or r < 0 or c < 0 or r >= m or c >= n or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            # explore neighbors
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # Start DFS from Pacific borders (top row, left col)
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])
        
        # Intersection
        result = list(pacific & atlantic)
        return result
