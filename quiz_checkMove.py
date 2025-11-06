class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        board[rMove][cMove] = color
        opp = 'B' if color == 'W' else 'W'
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def valid(i, j, di, dj):
            i += di
            j += dj
            count = 0
            while 0 <= i < 8 and 0 <= j < 8 and board[i][j] == opp:
                i += di
                j += dj
                count += 1
            if count > 0 and 0 <= i < 8 and 0 <= j < 8 and board[i][j] == color:
                return True
            return False

        for di, dj in dirs:
            if valid(rMove, cMove, di, dj):
                return True
        return False
