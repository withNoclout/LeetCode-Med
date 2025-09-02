class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort by x asc, y desc
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        n = len(points)
        for i in range(n):
            yi = points[i][1]
            maxY = -10**10
            for j in range(i + 1, n):
                yj = points[j][1]
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj
        return ans
