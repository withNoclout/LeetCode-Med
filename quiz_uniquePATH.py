import sys

# Increase recursion depth to handle long mirror chains or grid paths
sys.setrecursionlimit(10**6)

class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Memoization for the destination of a move entering (r, c) with direction d
        # Key: (r, c, direction)
        # Value: (final_r, final_c) or None (if out of bounds)
        # Direction: 0 = Moving Right, 1 = Moving Down
        memo_jump = {}

        def get_landing(r, c, d):
            # Check boundaries
            if not (0 <= r < m and 0 <= c < n):
                return None
            
            # If it's an empty cell, the movement stops/lands here
            if grid[r][c] == 0:
                return (r, c)
            
            # If we have already computed this mirror chain state
            state = (r, c, d)
            if state in memo_jump:
                return memo_jump[state]
            
            # Mirror Reflection Logic:
            # If moving Right (0) -> Hit Mirror -> Reflect Down (1) -> Move to (r+1, c)
            # If moving Down (1) -> Hit Mirror -> Reflect Right (0) -> Move to (r, c+1)
            if d == 0:
                res = get_landing(r + 1, c, 1)
            else:
                res = get_landing(r, c + 1, 0)
            
            memo_jump[state] = res
            return res

        # Memoization for the number of paths from (r, c) to (m-1, n-1)
        memo_paths = {}

        def solve(r, c):
            # Base Case: Reached destination
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in memo_paths:
                return memo_paths[(r, c)]
            
            total_paths = 0
            
            # Try moving Right from current empty cell
            # We enter (r, c+1) moving Right (0)
            landing_right = get_landing(r, c + 1, 0)
            if landing_right:
                lr, lc = landing_right
                total_paths = (total_paths + solve(lr, lc)) % MOD
            
            # Try moving Down from current empty cell
            # We enter (r+1, c) moving Down (1)
            landing_down = get_landing(r + 1, c, 1)
            if landing_down:
                dr, dc = landing_down
                total_paths = (total_paths + solve(dr, dc)) % MOD
            
            memo_paths[(r, c)] = total_paths
            return total_paths

        return solve(0, 0)
