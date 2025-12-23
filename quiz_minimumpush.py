class Solution(object):
    def minimumPushes(self, word):
        import collections
        counts = collections.Counter(word)
        freqs = sorted(counts.values(), reverse=True)
        
        res = 0
        for i, f in enumerate(freqs):
            res += f * (i // 8 + 1)
            
        return res
