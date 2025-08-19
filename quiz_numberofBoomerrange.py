class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for i in points:
            dist_count = {}
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist = dx*dx + dy*dy
                dist_count[dist] = dist_count.get(dist, 0) + 1
            for cnt in dist_count.values():
                res += cnt * (cnt - 1)  # permutations
        return res
