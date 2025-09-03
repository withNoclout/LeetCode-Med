class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def win(ch):
            b = board
            for i in range(3):
                if all(b[i][j] == ch for j in range(3)):  # rows
                    return True
                if all(b[j][i] == ch for j in range(3)):  # cols
                    return True
            if all(board[i][i] == ch for i in range(3)):
                return True
            if all(board[i][2 - i] == ch for i in range(3)):
                return True
            return False

        x = sum(row.count('X') for row in board)
        o = sum(row.count('O') for row in board)

        # X goes first: counts must be valid
        if not (x == o or x == o + 1):
            return False

        xwin = win('X')
        owin = win('O')

        # both can't win
        if xwin and owin:
            return False
        # if X wins, must have one more X than O
        if xwin and x != o + 1:
            return False
        # if O wins, counts must be equal
        if owin and x != o:
            return False

        return True
