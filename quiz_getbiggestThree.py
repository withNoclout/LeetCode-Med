class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                k = 1
                while i - k >= 0 and i + k < m and j - k >= 0 and j + k < n:
                    total = 0
                    x, y = i - k, j
                    while x < i:
                        total += grid[x][y]
                        x += 1
                        y -= 1
                    while y < j:
                        total += grid[x][y]
                        x += 1
                        y += 1
                    while x > i:
                        total += grid[x][y]
                        x -= 1
                        y += 1
                    while y > j:
                        total += grid[x][y]
                        x -= 1
                        y -= 1
                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]
