class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9 + 7
        total_ones = s.count('1')

        if total_ones % 3 != 0:
            return 0
        if total_ones == 0:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % mod

        ones_per_part = total_ones // 3
        count = 0
        first_cut = second_cut = 0

        for ch in s:
            if ch == '1':
                count += 1
            if count == ones_per_part:
                first_cut += 1
            elif count == ones_per_part + 1:
                break

        count = 0
        for ch in reversed(s):
            if ch == '1':
                count += 1
            if count == ones_per_part:
                second_cut += 1
            elif count == ones_per_part + 1:
                break

        return (first_cut * second_cut) % mod
