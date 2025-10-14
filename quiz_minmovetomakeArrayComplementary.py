class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # Sweep-line over all possible target sums s in [2, 2*limit].
        # For each pair (a, b), default need 2 moves for any s.
        # Improve to 1 move for s in [min(a,b)+1, max(a,b)+limit].
        # Improve to 0 moves exactly at s = a + b.
        n = len(nums)
        diff = [0] * (2 * limit + 2)  # difference array over sums

        i, j = 0, n - 1
        while i < j:
            a, b = nums[i], nums[j]
            lo, hi = min(a, b), max(a, b)

            # baseline: +2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # one move range
            diff[lo + 1] -= 1
            diff[hi + limit + 1] += 1

            # zero move at exact sum
            s = a + b
            diff[s] -= 1
            diff[s + 1] += 1

            i += 1
            j -= 1

        # prefix sum to get moves for each s and take the minimum
        ans = float('inf')
        cur = 0
        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            if cur < ans:
                ans = cur
        return ans
