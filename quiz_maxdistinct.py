class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The maximum number of substrings with distinct starts is bounded 
        # by the number of distinct characters available in the string.
        # We can always achieve this maximum by starting a new substring 
        # exactly when we see a character for the first time.
        return len(set(s))
