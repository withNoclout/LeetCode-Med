class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_count = {}
        right_count = {}

        for ch in s:
            right_count[ch] = right_count.get(ch, 0) + 1

        res = 0
        for ch in s:
            left_count[ch] = left_count.get(ch, 0) + 1
            right_count[ch] -= 1
            if right_count[ch] == 0:
                del right_count[ch]
            if len(left_count) == len(right_count):
                res += 1
        return res
