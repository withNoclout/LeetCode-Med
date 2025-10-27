class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        # accumulate heights of consecutive 1s column-wise
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        res = 0
        # for each row, sort heights descending → simulate rearranging columns
        for row in matrix:
            row.sort(reverse=True)
            for j, h in enumerate(row):
                res = max(res, h * (j + 1))
        return res
