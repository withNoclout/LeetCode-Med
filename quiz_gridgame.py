class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        top_rem = sum(grid[0])
        bottom_acc = 0
        ans = float('inf')

        for j in range(n):
            top_rem -= grid[0][j]              # cells remaining on top if switch after j
            ans = min(ans, max(top_rem, bottom_acc))
            bottom_acc += grid[1][j]           # cells collected on bottom before next column

        return ans
