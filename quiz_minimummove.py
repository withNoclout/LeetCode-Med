class Solution(object):
    def minimumMoves(self, grid):
        import itertools
        
        zeros = []
        extras = []
        
        for r in range(3):
            for c in range(3):
                if grid[r][c] == 0:
                    zeros.append((r, c))
                elif grid[r][c] > 1:
                    for _ in range(grid[r][c] - 1):
                        extras.append((r, c))
                        
        min_moves = float('inf')
        
        for p in itertools.permutations(extras):
            current_moves = 0
            for (zr, zc), (er, ec) in zip(zeros, p):
                current_moves += abs(zr - er) + abs(zc - ec)
            min_moves = min(min_moves, current_moves)
            
        return min_moves
