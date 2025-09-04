class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        row = [0.0] * (query_row + 2)
        row[0] = float(poured)
        for r in range(query_row):
            next_row = [0.0] * (query_row + 2)
            for c in range(r + 1):
                overflow = max(0.0, row[c] - 1.0)
                if overflow > 0:
                    share = overflow / 2.0
                    next_row[c] += share
                    next_row[c + 1] += share
            for c in range(r + 2):
                row[c] = min(1.0, row[c]) + next_row[c]  # cap current, pass overflow separately
        return min(1.0, row[query_glass])
