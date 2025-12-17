class Solution(object):
    def countPairs(self, coordinates, k):
        import collections
        counts = collections.defaultdict(int)
        res = 0
        
        for x, y in coordinates:
            for val in range(k + 1):
                # If (x ^ tx) = val, then tx = x ^ val
                # If (y ^ ty) = k - val, then ty = y ^ (k - val)
                tx = x ^ val
                ty = y ^ (k - val)
                
                res += counts[(tx, ty)]
                
            counts[(x, y)] += 1
            
        return res
