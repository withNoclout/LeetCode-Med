class Solution(object):
    def takeCharacters(self, s, k):
        count = {c: s.count(c) for c in 'abc'}
        if any(count[c] < k for c in 'abc'): return -1
        
        limit = {c: count[c] - k for c in 'abc'}
        cur = {'a': 0, 'b': 0, 'c': 0}
        res = left = 0
        
        for right, c in enumerate(s):
            cur[c] += 1
            while cur[c] > limit[c]:
                cur[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            
        return len(s) - res
