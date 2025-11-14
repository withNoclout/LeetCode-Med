class Solution(object):
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 <= n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 <= n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 <= n and c2 + 1 <= n:
                diff[r2 + 1][c2 + 1] += 1

        # Prefix sum horizontally
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # Prefix sum vertically
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Extract top-left n x n
        return [row[:n] for row in diff[:n]]
