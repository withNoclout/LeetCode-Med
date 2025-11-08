from collections import defaultdict

class DetectSquares(object):

    def __init__(self):
        # Count how many times each (x, y) point has been added
        self.points = defaultdict(int)
        # For faster lookup by x coordinate
        self.points_by_x = defaultdict(list)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.points[(x, y)] += 1
        self.points_by_x[x].append(y)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        if x not in self.points_by_x:
            return 0

        total = 0
        # For each point with the same x coordinate
        for ny in self.points_by_x[x]:
            if ny == y:
                continue
            side = abs(ny - y)
            # Two possible squares: to the left or to the right
            for nx in (x + side, x - side):
                total += (
                    self.points[(x, ny)] *
                    self.points[(nx, y)] *
                    self.points[(nx, ny)]
                )
        return total
