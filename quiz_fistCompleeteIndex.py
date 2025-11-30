class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        coords = {mat[r][c]: (r, c) for r in range(m) for c in range(n)}
        row_cnt = [0] * m
        col_cnt = [0] * n
        
        for i, num in enumerate(arr):
            r, c = coords[num]
            row_cnt[r] += 1
            col_cnt[c] += 1
            if row_cnt[r] == n or col_cnt[c] == m:
                return i
        return -1
