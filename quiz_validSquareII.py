class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def dist(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
        dists = []

        # compute all pairwise distances
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(dist(points[i], points[j]))

        dists.sort()

        # 4 equal small distances (sides), 2 equal large distances (diagonals)
        return (
            dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5] and
            dists[4] == 2 * dists[0]
        )

