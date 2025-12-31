class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        counts = Counter(s)
        ans = 0
        
        for count in counts.values():
            if count % 2 == 1:
                ans += 1
            else:
                ans += 2
                
        return ans

        
