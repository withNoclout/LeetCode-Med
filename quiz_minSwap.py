class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = s.count('1')
        zeros = len(s) - ones
        if abs(ones - zeros) > 1:
            return -1

        def count_mismatch(start_char):
            mismatch = 0
            for i, ch in enumerate(s):
                expected = start_char if i % 2 == 0 else ('1' if start_char == '0' else '0')
                if ch != expected:
                    mismatch += 1
            return mismatch // 2

        if ones > zeros:
            return count_mismatch('1')
        elif zeros > ones:
            return count_mismatch('0')
        else:
            return min(count_mismatch('0'), count_mismatch('1'))
