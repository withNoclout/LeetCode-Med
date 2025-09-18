class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        patterns = []
        for row in matrix:
            # Normalize row: flip if first element is 1
            if row[0] == 1:
                patterns.append(tuple(1 - x for x in row))
            else:
                patterns.append(tuple(row))
        return Counter(patterns).most_common(1)[0][0] if patterns else 0
