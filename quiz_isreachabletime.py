class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        width = abs(sx - fx)
        height = abs(sy - fy)
        min_dist = max(width, height)
        
        if min_dist == 0 and t == 1:
            return False
            
        return t >= min_dist
