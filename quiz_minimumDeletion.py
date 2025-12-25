class Solution(object):
    def minimumDeletions(self, word, k):
        import collections
        freqs = sorted(collections.Counter(word).values())
        res = float('inf')
        
        # Try each existing frequency as the minimum frequency (base)
        for min_f in freqs:
            ops = 0
            for f in freqs:
                if f < min_f:
                    # If freq is less than base, delete all characters
                    ops += f
                elif f > min_f + k:
                    # If freq exceeds limit, reduce to base + k
                    ops += f - (min_f + k)
            res = min(res, ops)
            
        return res
