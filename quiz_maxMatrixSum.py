class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        neg = 0
        min_abs = float('inf')
        for row in matrix:
            for v in row:
                if v < 0:
                    neg ^= 1  # track parity of negatives
                av = abs(v)
                total += av
                if av < min_abs:
                    min_abs = av
        return total if neg == 0 else total - 2 * min_abs

