class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(
                    matrix[i-1][j],
                    matrix[i-1][j-1] if j > 0 else float('inf'),
                    matrix[i-1][j+1] if j < n-1 else float('inf')
                )
        return min(matrix[-1])
