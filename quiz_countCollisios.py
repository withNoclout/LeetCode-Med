class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions.lstrip('L').rstrip('R')
        return len(s) - s.count('S')
