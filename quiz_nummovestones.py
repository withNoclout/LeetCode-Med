class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted([a, b, c])
        min_moves = 0
        if y - x > 1:
            min_moves += 1
        if z - y > 1:
            min_moves += 1
        if y - x == 2 or z - y == 2:
            min_moves = 1
        max_moves = z - x - 2
        return [min_moves, max_moves]
