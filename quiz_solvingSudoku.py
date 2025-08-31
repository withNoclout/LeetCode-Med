class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        N = 9
        ALL = (1 << 9) - 1  # bits 0..8 represent digits 1..9

        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        # init masks
        for r in range(N):
            for c in range(N):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = ord(ch) - ord('1')  # 0..8
                    bit = 1 << d
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_id(r, c)] |= bit

        def dfs(i=0):
            if i == len(empties):
                return True

            # choose cell with minimal candidates (heuristic)
            min_idx = i
            min_candidates = ALL + 1
            for j in range(i, len(empties)):
                r, c = empties[j]
                used = rows[r] | cols[c] | boxes[box_id(r, c)]
                cand = ALL & ~used
                # count bits
                cnt = 0
                x = cand
                while x:
                    x &= x - 1
                    cnt += 1
                if cnt < min_candidates:
                    min_candidates = cnt
                    min_idx = j
                    if cnt == 1:
                        break
            empties[i], empties[min_idx] = empties[min_idx], empties[i]
            r, c = empties[i]
            used = rows[r] | cols[c] | boxes[box_id(r, c)]
            cand = ALL & ~used
            b = box_id(r, c)

            while cand:
                bit = cand & -cand
                cand -= bit
                d = (bit.bit_length() - 1)  # 0..8
                board[r][c] = chr(ord('1') + d)
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if dfs(i + 1):
                    return True

                # undo
                rows[r] &= ~bit
                cols[c] &= ~bit
                boxes[b] &= ~bit
                board[r][c] = '.'

            return False

        dfs()
