class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ALL = (1 << n) - 1

        # pal_len[mask] = length if subsequence(mask) is palindrome else 0
        pal_len = [0] * (1 << n)

        for mask in range(1, 1 << n):
            # collect indices selected by mask
            idx = []
            m = mask
            i = 0
            while m:
                if m & 1:
                    idx.append(i)
                i += 1
                m >>= 1

            l, r = 0, len(idx) - 1
            ok = True
            while l < r:
                if s[idx[l]] != s[idx[r]]:
                    ok = False
                    break
                l += 1
                r -= 1
            if ok:
                pal_len[mask] = len(idx)

        # best[mask] = max pal_len[sub] for all sub ⊆ mask (SOS DP)
        best = pal_len[:]
        for i in range(n):
            bit = 1 << i
            for mask in range(1 << n):
                if mask & bit:
                    if best[mask ^ bit] > best[mask]:
                        best[mask] = best[mask ^ bit]

        ans = 0
        for mask in range(1, 1 << n):
            if pal_len[mask]:
                rem = ALL ^ mask
                prod = pal_len[mask] * best[rem]
                if prod > ans:
                    ans = prod
        return ans
