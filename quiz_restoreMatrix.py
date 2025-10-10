class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]
        i = j = 0
        rs = rowSum[:]
        cs = colSum[:]
        while i < m and j < n:
            x = min(rs[i], cs[j])
            ans[i][j] = x
            rs[i] -= x
            cs[j] -= x
            if rs[i] == 0:
                i += 1
            if cs[j] == 0:
                j += 1
        return ans
