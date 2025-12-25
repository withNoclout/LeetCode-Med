class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        mid = n // 2
        y_cnt = [0] * 3
        non_y_cnt = [0] * 3
        
        for r in range(n):
            for c in range(n):
                # Check if cell (r, c) is part of the 'Y' shape
                is_y = (r <= mid and (r == c or r + c == n - 1)) or (r > mid and c == mid)
                
                if is_y:
                    y_cnt[grid[r][c]] += 1
                else:
                    non_y_cnt[grid[r][c]] += 1
        
        total_y = sum(y_cnt)
        total_non = sum(non_y_cnt)
        res = float('inf')
        
        # Try all combinations of values (0, 1, 2) for Y and Non-Y parts
        for i in range(3):
            for j in range(3):
                if i == j: continue
                # Ops = (Cells in Y not matching i) + (Cells not in Y not matching j)
                ops = (total_y - y_cnt[i]) + (total_non - non_y_cnt[j])
                res = min(res, ops)
                
        return res
