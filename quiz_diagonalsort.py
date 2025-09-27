class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        # Collect all elements in the same diagonal (key = i - j)
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])

        # Sort each diagonal in reverse (so we can pop from end)
        for key in diagonals:
            diagonals[key].sort(reverse=True)

        # Refill the matrix with sorted values
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        return mat
