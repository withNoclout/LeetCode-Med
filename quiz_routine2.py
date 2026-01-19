class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Precompute prefix sums for rows and columns
        # row_sum[i][j] = sum(grid[i][0]...grid[i][j-1])
        row_sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                
        # col_sum[i][j] = sum(grid[0][j]...grid[i-1][j])
        col_sum = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]

        # Iterate size k from largest possible down to 2
        for k in range(min(m, n), 1, -1):
            # Iterate through all possible top-left corners (r, c)
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    # Calculate the target sum from the first row of the square
                    target = row_sum[r][c + k] - row_sum[r][c]
                    
                    match = True
                    
                    # Check all rows
                    for i in range(1, k):
                        if (row_sum[r + i][c + k] - row_sum[r + i][c]) != target:
                            match = False
                            break
                    if not match: continue
                    
                    # Check all columns
                    for j in range(k):
                        if (col_sum[r + k][c + j] - col_sum[r][c + j]) != target:
                            match = False
                            break
                    if not match: continue
                    
                    # Check main diagonal
                    d1 = 0
                    for i in range(k):
                        d1 += grid[r + i][c + i]
                    if d1 != target: continue
                    
                    # Check anti-diagonal
                    d2 = 0
                    for i in range(k):
                        d2 += grid[r + i][c + k - 1 - i]
                    if d2 != target: continue
                    
                    return k
                    
        return 1
