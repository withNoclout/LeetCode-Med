import bisect

class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        # heights are in [1, 100]
        buckets = [[] for _ in range(101)]
        for l, h in rectangles:
            buckets[h].append(l)

        for h in range(1, 101):
            buckets[h].sort()

        res = []
        for x, y in points:
            cnt = 0
            for h in range(y, 101):
                arr = buckets[h]
                if arr:
                    idx = bisect.bisect_left(arr, x)
                    cnt += len(arr) - idx
            res.append(cnt)

        return res
