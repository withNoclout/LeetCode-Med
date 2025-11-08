class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        L = len(word)
        wrev = word[::-1]

        def fits(segment, w):
            if len(segment) != L:
                return False
            for a, b in zip(segment, w):
                if a != ' ' and a != b:
                    return False
            return True

        # Check rows
        for i in range(m):
            j = 0
            while j < n:
                if board[i][j] == '#':
                    j += 1
                    continue
                start = j
                while j < n and board[i][j] != '#':
                    j += 1
                seg = [board[i][k] for k in range(start, j)]
                if fits(seg, word) or fits(seg, wrev):
                    return True

        # Check columns
        for j in range(n):
            i = 0
            while i < m:
                if board[i][j] == '#':
                    i += 1
                    continue
                start = i
                while i < m and board[i][j] != '#':
                    i += 1
                seg = [board[k][j] for k in range(start, i)]
                if fits(seg, word) or fits(seg, wrev):
                    return True

        return False
