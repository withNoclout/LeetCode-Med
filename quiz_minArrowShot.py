class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # sort by ending coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]

        for start, finish in points[1:]:
            if start > end:   # need a new arrow
                arrows += 1
                end = finish

        return arrows
