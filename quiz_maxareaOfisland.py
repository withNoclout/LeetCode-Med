class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]  :
            return 0 
        
        rows , cols = len(grid ) , len(grid[0]) 

        ans = 0 
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for r in range(rows ) :
            for c in range(cols ) :
                if grid[r][c] == 1 : 
                    area =  0 
                    stack = [(r,c)]
                    while stack :
                        x,y = stack.pop()
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                            grid[x][y] = 0
                            area += 1
                            for dx, dy in dirs:
                                stack.append((x+dx, y+dy))
                    ans = max(ans, area)
        return ans
