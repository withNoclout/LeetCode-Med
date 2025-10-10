import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        if not towers:
            return [0, 0]
        xs = [t[0] for t in towers]
        ys = [t[1] for t in towers]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)

        best = -1
        ans = [0, 0]
        r2 = radius * radius

        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                total = 0
                for tx, ty, q in towers:
                    dx = x - tx
                    dy = y - ty
                    d2 = dx * dx + dy * dy
                    if d2 <= r2:
                        d = math.sqrt(d2)
                        total += int(q / (1 + d))
                if total > best or (total == best and (x < ans[0] or (x == ans[0] and y < ans[1]))):
                    best = total
                    ans = [x, y]
        return ans
