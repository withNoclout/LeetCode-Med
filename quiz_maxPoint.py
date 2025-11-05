class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        def slope(p1, p2):
            if p1[0] == p2[0]:
                return float('inf')
            return float(p2[1] - p1[1]) / (p2[0] - p1[0])

        res = 0
        for i in range(len(points)):
            slopes = {}
            same = 1
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same += 1
                else:
                    s = slope(points[i], points[j])
                    slopes[s] = slopes.get(s, 0) + 1
            res = max(res, same)
            for val in slopes.values():
                res = max(res, val + same)
        return res
