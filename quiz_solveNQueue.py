class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col_set = set()
        pos_diag = set()  # Tracks r + c
        neg_diag = set()  # Tracks r - c
        
        res = []
        # Initialize an empty board
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            # Base case: All queens are placed successfully
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                # Check if the current cell is under attack
                if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # 1. Place the queen and mark the attack vectors
                col_set.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # 2. Recurse to the next row
                backtrack(r + 1)
                
                # 3. Backtrack: Remove the queen and clear the attack vectors
                col_set.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        # Start backtracking from the first row
        backtrack(0)
        return res
