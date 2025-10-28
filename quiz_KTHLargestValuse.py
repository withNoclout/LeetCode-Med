class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        vals = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] ^ prefix[i][j - 1] ^ prefix[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                vals.append(prefix[i][j])
        vals.sort(reverse=True)
        return vals[k - 1]
