class Solution(object):
    def matrixSumQueries(self, n, queries):
        seen_rows = set()
        seen_cols = set()
        total = 0
        
        for type, index, val in reversed(queries):
            if type == 0:
                if index not in seen_rows:
                    total += val * (n - len(seen_cols))
                    seen_rows.add(index)
            else:
                if index not in seen_cols:
                    total += val * (n - len(seen_rows))
                    seen_cols.add(index)
                    
        return total
