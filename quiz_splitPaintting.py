class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        # Use line sweep technique: track color changes at start and end points
        diff = defaultdict(int)
        for start, end, color in segments:
            diff[start] += color
            diff[end] -= color

        res = []
        prev = None
        cur_color = 0

        for point in sorted(diff.keys()):
            if prev is not None and cur_color > 0:
                res.append([prev, point, cur_color])
            cur_color += diff[point]
            prev = point

        return res
