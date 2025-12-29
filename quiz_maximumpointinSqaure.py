class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        min1 = {}
        limit = float('inf')
        
        for i, (x, y) in enumerate(points):
            d = max(abs(x), abs(y))
            c = s[i]
            
            if c not in min1:
                min1[c] = d
            elif d < min1[c]:
                limit = min(limit, min1[c])
                min1[c] = d
            else:
                limit = min(limit, d)
                
        count = 0
        for x, y in points:
            if max(abs(x), abs(y)) < limit:
                count += 1
        return count
