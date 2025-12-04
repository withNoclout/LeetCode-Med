class Solution(object):
    def countCollisions(self, directions):
        s = directions.lstrip('L').rstrip('R')
        return len(s) - s.count('S')
