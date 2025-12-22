class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        h_gaps = {b - a for i, a in enumerate(h) for b in h[i+1:]}
        v_gaps = {b - a for i, a in enumerate(v) for b in v[i+1:]}
        
        common = h_gaps & v_gaps
        return max(common)**2 % (10**9 + 7) if common else -1
