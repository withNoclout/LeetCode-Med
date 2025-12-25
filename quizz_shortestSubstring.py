class Solution(object):
    def shortestSubstrings(self, arr):
        res = []
        for i, s in enumerate(arr):
            n = len(s)
            candidates = set()
            for length in range(1, n + 1):
                for start in range(n - length + 1):
                    candidates.add(s[start : start + length])
            
            # Sort by length first, then lexicographically
            sorted_cands = sorted(list(candidates), key=lambda x: (len(x), x))
            
            ans = ""
            for sub in sorted_cands:
                valid = True
                for j, other in enumerate(arr):
                    if i != j and sub in other:
                        valid = False
                        break
                if valid:
                    ans = sub
                    break
            res.append(ans)
        return res
