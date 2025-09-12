class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n, m = len(strs), len(strs[0])
        res = 0
        sorted_rows = [False] * (n - 1)
        for col in range(m):
            for row in range(n - 1):
                if not sorted_rows[row] and strs[row][col] > strs[row + 1][col]:
                    res += 1
                    break
            else:
                for row in range(n - 1):
                    if strs[row][col] < strs[row + 1][col]:
                        sorted_rows[row] = True
        return res
