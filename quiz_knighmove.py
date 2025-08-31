class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] != 0.0:
                        p = dp[r][c] / 8.0
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                ndp[nr][nc] += p
            dp = ndp

        return sum(map(sum, dp))
