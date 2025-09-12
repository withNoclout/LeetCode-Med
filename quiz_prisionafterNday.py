class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n
            if n > 0:
                n -= 1
                cells = [0] + [int(cells[i-1] == cells[i+1]) for i in range(1, 7)] + [0]
        return cells
