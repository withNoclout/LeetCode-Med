class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        x, y = click

        if board[x][y] == "M":  # clicked a mine
            board[x][y] = "X"
            return board

        def count_mines(i, j):
            cnt = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "M":
                        cnt += 1
            return cnt

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != "E":
                return
            mines = count_mines(i, j)
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = "B"
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        dfs(i + dx, j + dy)

        dfs(x, y)
        return board
