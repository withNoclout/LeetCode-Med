class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort by x asc, y desc to ensure for equal x we only count once
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        n = len(points)
        for i in range(n):
            yi = points[i][1]
            best = -10**10
            for j in range(i + 1, n):
                yj = points[j][1]
                if yi >= yj > best:
                    ans += 1
                    best = yj
        return ans
