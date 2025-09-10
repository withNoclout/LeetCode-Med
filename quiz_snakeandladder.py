# ...existing code...
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0]:
            return -1

        from collections import deque
        n = len(board)

        def dest_value(square):
            # square is 1-based
            r = (square - 1) // n
            c = (square - 1) % n
            row = n - 1 - r
            col = c if (r % 2 == 0) else (n - 1 - c)
            val = board[row][col]
            return val if val != -1 else square

        target = n * n
        q = deque([(1, 0)])  # (square, moves)
        visited = [False] * (target + 1)
        visited[1] = True

        while q:
            square, moves = q.popleft()
            if square == target:
                return moves
            for step in range(1, 7):
                nxt = square + step
                if nxt > target:
                    break
                val = dest_value(nxt)
                if val == target:
                    return moves + 1
                if not visited[val]:
                    visited[val] = True
                    q.append((val, moves + 1))
        return -1
#
