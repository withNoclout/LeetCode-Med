class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]  : 
            return 
        
        rows , cols = len(board )  , len(board[0] ) 

        def dfs( r, c ) :
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != '0' : 
                return 
            
            board[r][c] = '1' 
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)   
            dfs(r, c + 1)

        for r in range(rows ) :
            dfs( r,  0 ) 
            dfs( r, cols - 1 ) 

        for c in range( cols ) :
            dfs( 0, c ) 
            dfs( rows - 1, c )  


        for r in range(rows ) :
            for c in range(cols ) :
                if board[r][c] == '0' :
                    board[r][c] = 'X'


                elif board[r][c] == 'E' : 
                    board[r][c] = '0'



