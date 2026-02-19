class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev_count = 0
        curr_count = 1
        
        for i in range(1, len(s)):
            # If the character changed, the current group is finished
            if s[i] != s[i-1]:
                # We can form min(prev, curr) substrings between these two groups
                ans += min(prev_count, curr_count)
                # Current group becomes the previous group
                prev_count = curr_count
                curr_count = 1
            else:
                # Still in the same group
                curr_count += 1
        
        # Don't forget the very last transition!
        return ans + min(prev_count, curr_count)
