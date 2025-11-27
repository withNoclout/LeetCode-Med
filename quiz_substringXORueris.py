class Solution(object):
    def substringXorQueries(self, s, queries):
        seen = {}
        n = len(s)
        
        for i in range(n):
            val = 0
            # Iterate through substrings starting at i with max length 32
            # (sufficient for 10^9 range queries)
            for j in range(i, min(n, i + 32)):
                val = (val << 1) | int(s[j])
                if val not in seen:
                    seen[val] = [i, j]
                
                # Optimization: if val exceeds max possible query result, break
                if val > 2 * 10**9:
                    break
                    
        res = []
        for first, second in queries:
            target = first ^ second
            res.append(seen.get(target, [-1, -1]))
        return res
