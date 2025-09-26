class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # Count mismatches
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1

        # If total mismatches are odd, impossible
        if (xy + yx) % 2 == 1:
            return -1

        # Pairs of xy can be fixed with xy//2 swaps, same for yx
        # Remaining 1 xy + 1 yx requires 2 swaps
        return xy // 2 + yx // 2 + (xy % 2) * 2
