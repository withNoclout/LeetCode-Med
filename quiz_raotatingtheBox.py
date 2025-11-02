class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(boxGrid), len(boxGrid[0])
        for row in boxGrid:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1

        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]
        return res
