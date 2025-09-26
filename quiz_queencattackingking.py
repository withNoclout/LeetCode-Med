class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queen_set = {(x, y) for x, y in queens}
        res = []
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dx, dy in directions:
            x, y = king
            while 0 <= x+dx < 8 and 0 <= y+dy < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
        return res
