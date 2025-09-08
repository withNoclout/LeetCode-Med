# ...existing code...
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        total = rows * cols
        res = []
        r, c = rStart, cStart
        if 0 <= r < rows and 0 <= c < cols:
            res.append([r, c])

        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        while len(res) < total:
            for i, (dr, dc) in enumerate(dirs):
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                if i % 2 == 1:
                    steps += 1

        return res
