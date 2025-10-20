class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        total = pref[n]

        ans = 0
        l = r = 1  # j pointers for middle split (i < j < n)

        for i in range(1, n - 1):  # i is end index of left part -> left sum = pref[i]
            left = pref[i]
            # advance l to the first j such that mid >= left
            l = max(l, i + 1)
            while l < n and pref[l] - left < left:
                l += 1

            # advance r to the last j such that mid <= right
            r = max(r, l)
            while r < n and pref[r] - left <= total - pref[r]:
                r += 1  # r stops at first invalid, so valid j are [l, r-1]

            ans += max(0, r - l)
            ans %= MOD

        return ans
