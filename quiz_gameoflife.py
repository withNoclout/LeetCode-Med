class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m ,n = len(board ) , len(board[0] ) 
        def count_live_neighbors( r, c ) :
            count = 0 
            for dr in ( -1 , 0 , 1 ) :
                for dc in ( -1 , 0 , 1 ) :
                    if dr == 0 and dc == 0 :
                        continue 
                    nr , nc = r + dr , c + dc 
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 1 :
                        count += 1
            return count 
        
        for r in range(m) :
            for c in range(n) :
                live_neighbors = count_live_neighbors(r, c)

                if board[r][c] & 1 : 
                    if live_neighbors == 1 or live_neighbors == 2 or live_neighbors == 3:
                        board[r][c] |= 2 
                else : 
                    if live_neighbors == 3 :
                        board[r][c] |= 2 
        for r in range(m)  :
            for c in range(n) :
                board[r][c] >>= 1 
                
