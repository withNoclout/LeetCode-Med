class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        res = []

        for i in range(m):
            for j in range(n):
                if land[i][j] != 1:
                    continue
                if (i > 0 and land[i - 1][j] == 1) or (j > 0 and land[i][j - 1] == 1):
                    continue  # not a top-left corner

                # find bottom boundary
                r = i
                while r + 1 < m and land[r + 1][j] == 1:
                    r += 1
                # find right boundary
                c = j
                while c + 1 < n and land[i][c + 1] == 1:
                    c += 1

                res.append([i, j, r, c])
        return res
