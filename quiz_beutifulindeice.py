class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        def get_indices(sub):
            res = []
            i = s.find(sub)
            while i != -1:
                res.append(i)
                i = s.find(sub, i + 1)
            return res

        indices_a = get_indices(a)
        indices_b = get_indices(b)
        
        import bisect
        ans = []
        for i in indices_a:
            # Find first index in b that is >= i - k
            idx = bisect.bisect_left(indices_b, i - k)
            if idx < len(indices_b) and indices_b[idx] <= i + k:
                ans.append(i)
                
        return ans
