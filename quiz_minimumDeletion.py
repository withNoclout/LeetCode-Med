class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count_b tracks the number of 'b's encountered so far
        count_b = 0
        # deletions tracks the minimum deletions needed to balance the string processed so far
        deletions = 0
        
        for char in s:
            if char == 'b':
                # If we see a 'b', it doesn't immediately cause a conflict,
                # so we just increment our count of 'b's.
                count_b += 1
            else:
                # If we see an 'a', we have a potential conflict with previous 'b's.
                # We have two choices to resolve this:
                # 1. Delete the current 'a'. Cost = (current deletions) + 1
                # 2. Keep the current 'a'. To do this, we must have removed all 
                #    preceding 'b's. Cost = count_b
                
                # We take the minimum of these two options.
                deletions = min(deletions + 1, count_b)
                
        return deletionsclass Solution(object):
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
