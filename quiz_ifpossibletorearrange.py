from collections import Counter

class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        size = n // k
        
        # Split both strings into k segments of equal size
        s_segments = [s[i : i + size] for i in range(0, n, size)]
        t_segments = [t[i : i + size] for i in range(0, n, size)]
        
        # Check if the frequency of segments is the same
        return Counter(s_segments) == Counter(t_segments)
