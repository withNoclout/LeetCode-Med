class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        first = {}
        last = {}
        
        # Record first and last indices of each character
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        intervals = []
        unique_chars = list(first.keys())
        
        # Iterate over all possible start (first occurrence) and end (last occurrence) characters
        for c_start in unique_chars:
            start = first[c_start]
            for c_end in unique_chars:
                end = last[c_end]
                
                if start > end: 
                    continue
                
                # Check if s[start:end+1] is a valid special substring
                # A substring is valid if for every char inside it, 
                # all occurrences of that char are also inside it.
                valid = True
                for char in unique_chars:
                    if start <= first[char] and last[char] <= end:
                        # Character is fully inside the range
                        continue
                    if last[char] < start or first[char] > end:
                        # Character is fully outside the range
                        continue
                    # Character crosses the boundary (invalid)
                    valid = False
                    break
                
                # We strictly need a proper substring (length < total length)
                if valid and (end - start + 1) < n:
                    intervals.append((start, end))
                    
        # Greedy Strategy: Sort by length (shortest first) to minimize overlap probability
        intervals.sort(key=lambda x: x[1] - x[0])
        
        res = []
        for start, end in intervals:
            # Check if disjoint from all currently selected intervals
            if all(end < s or start > e for s, e in res):
                res.append((start, end))
                
        return len(res) >= k
