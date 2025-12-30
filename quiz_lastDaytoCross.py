class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            grid = [[0] * col for _ in range(row)]
            for r, c in cells[:mid]:
                grid[r - 1][c - 1] = 1
            
            queue = []
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 2
            
            possible = False
            head = 0
            while head < len(queue):
                r, c = queue[head]
                head += 1
                if r == row - 1:
                    possible = True
                    break
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            
            if possible:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
