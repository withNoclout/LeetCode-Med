class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            col = max(range(n), key=lambda c: mat[mid][c])
            up = mat[mid - 1][col] if mid > 0 else -1
            down = mat[mid + 1][col] if mid < m - 1 else -1
            if mat[mid][col] > up and mat[mid][col] > down:
                return [mid, col]
            elif mat[mid][col] < down:
                top = mid + 1
            else:
                bottom = mid - 1
