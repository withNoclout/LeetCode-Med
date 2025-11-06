class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count unmatched closing brackets.
        # Each swap can fix two unmatched closings.
        open_cnt = 0
        unmatched = 0
        for ch in s:
            if ch == '[':
                open_cnt += 1
            else:
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    unmatched += 1
        return (unmatched + 1) // 2
