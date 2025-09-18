class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # Directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        x = y = d = 0
        for ch in instructions:
            if ch == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif ch == 'L':
                d = (d + 3) % 4
            else:  # 'R'
                d = (d + 1) % 4
        return (x == 0 and y == 0) or d != 0
