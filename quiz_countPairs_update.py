from collections import defaultdict

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not deliciousness:
            return 0

        max_val = max(deliciousness)
        max_sum = max_val * 2

        # Precompute all powers of two up to max_sum.
        powers = []
        p = 1
        while p <= max_sum:
            powers.append(p)
            p <<= 1

        freq = defaultdict(int)
        ans = 0

        for x in deliciousness:
            for p in powers:
                y = p - x
                if y in freq:
                    ans = (ans + freq[y]) % MOD
            freq[x] += 1

        return ans
