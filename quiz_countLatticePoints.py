class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        points = set()

        for x, y, r in circles:
            r2 = r * r
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r2:
                        points.add((i, j))

        return len(points)
