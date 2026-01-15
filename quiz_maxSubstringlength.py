class Solution(object):
    def maxSubstringLength(self, s, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if k == 0: return True
        
        n = len(s)
        first = {c: i for i, c in enumerate(s[::-1])} # Last occurrence
        first = {c: i for i, c in enumerate(s)}
        last = {c: n - 1 - i for i, c in enumerate(s[::-1])}
        
        intervals = []
        for char in first:
            l, r = first[char], last[char]
            if l == 0 and r == n - 1: continue # Must be a proper substring
            
            # Expand interval to include all occurrences of chars within
            possible = True
            curr_r = r
            i = l
            while i <= curr_r:
                char_at_i = s[i]
                if first[char_at_i] < l:
                    possible = False
                    break
                curr_r = max(curr_r, last[char_at_i])
                i += 1
            
            if possible and not (l == 0 and curr_r == n - 1):
                intervals.append([l, curr_r])
        
        # Interval Scheduling Maximization (Greedy)
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r
                
        return count >= k
