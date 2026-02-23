class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        col_set = set()
        pos_diag = set()  # Tracks r + c
        neg_diag = set()  # Tracks r - c
        
        def backtrack(r):
            # Base case: All queens placed successfully
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                # Check if cell is under attack
                if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place queen (mark attack vectors)
                col_set.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Recurse to next row
                backtrack(r + 1)
                
                # Backtrack: Remove queen (clear attack vectors)
                col_set.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        # Start backtracking from row 0
        backtrack(0)
        return self.count
