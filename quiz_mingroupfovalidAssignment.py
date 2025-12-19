class Solution(object):
    def minGroupsForValidAssignment(self, balls):
        import collections
        counts = collections.Counter(balls).values()
        min_c = min(counts)
        
        # Iterate box size k from max possible (min_c) down to 1
        for k in range(min_c, 0, -1):
            res = 0
            valid = True
            for c in counts:
                q, r = divmod(c, k)
                if q < r:
                    valid = False
                    break
                # Equivalent to ceil(c / (k + 1))
                res += (c + k) // (k + 1)
                
            if valid:
                return res
