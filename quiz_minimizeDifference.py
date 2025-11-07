class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        # Bitset DP: dp has bit s set iff sum s is achievable
        dp = 1  # only sum 0 achievable initially (bit 0)
        max_sum = 0

        for row in mat:
            # Use unique values to limit redundant shifts
            row_vals = set(row)
            nxt = 0
            for v in row_vals:
                nxt |= (dp << v)
            dp = nxt
            max_sum += max(row_vals)

        # Clamp dp to at most max_sum bits to keep it small
        if dp.bit_length() - 1 > max_sum:
            dp &= (1 << (max_sum + 1)) - 1

        # Find minimal absolute difference to target among achievable sums
        # Check sums near target outward.
        best = float('inf')
        # Bound search range: [0, max_sum]
        # Move outwards from target
        for d in range(0, max_sum + 1):
            s1 = target - d
            if 0 <= s1 <= max_sum and ((dp >> s1) & 1):
                return d
            s2 = target + d
            if 0 <= s2 <= max_sum and ((dp >> s2) & 1):
                return d
        return best
