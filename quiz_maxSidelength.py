class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        # Build 2D Prefix Sum Array
        # P[i][j] stores the sum of the rectangle from (0,0) to (i-1, j-1)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
        
        # Helper to get sum of square defined by (r1, c1) to (r2, c2)
        def getRectSum(r1, c1, r2, c2):
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

        max_side = 0
        
        # Iterate through every possible bottom-right corner (i, j)
        for i in range(m):
            for j in range(n):
                # We only care if we can find a larger square than we already have.
                # Check if a square of size (max_side + 1) ending at (i, j) is valid.
                target_len = max_side + 1
                
                # Ensure the square fits within the grid boundaries
                if i - target_len + 1 >= 0 and j - target_len + 1 >= 0:
                    current_sum = getRectSum(i - target_len + 1, j - target_len + 1, i, j)
                    if current_sum <= threshold:
                        max_side += 1
                        
        return max_side
