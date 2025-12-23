class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        count = collections.Counter(s)
        max_freq = max(count.values())
        
        res = []
        seen = set()
        # Iterate backwards to find the last occurrence of characters with max frequency
        for c in reversed(s):
            if count[c] == max_freq and c not in seen:
                res.append(c)
                seen.add(c)
                
        return "".join(res[::-1])
