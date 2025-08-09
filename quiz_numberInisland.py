class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0] :
            return 0 
        
        m , n = len(grid), len(grid[0])

        count =  0

        def sink( r , c) : 
            stack = [(r, c)]
            while stack : 
                i ,  j  = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == '1' :
                    grid[i][j] = '0'
                    stack.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += sink(i, j)

        return count
