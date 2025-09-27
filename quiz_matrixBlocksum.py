class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        # prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def get_sum(r1, c1, r2, c2):
            return ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m, i + k + 1)
                c2 = min(n, j + k + 1)
                res[i][j] = get_sum(r1, c1, r2, c2)
        return res
