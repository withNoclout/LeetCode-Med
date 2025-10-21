class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        # Idea:
        # Pick a target value v. Any element x can be turned into v in one op iff |x - v| <= k.
        # So for each distinct v, let:
        #   inRange(v) = count of numbers in [v - k, v + k]
        #   freqV      = original count of v
        # We can change at most `numOperations` of the in-range-but-not-v elements to v.
        # Achievable freq for v = min(inRange(v), freqV + numOperations).
        # Compute this for all distinct v efficiently using two pointers on the compressed values.
        if not nums:
            return 0

        nums.sort()

        # Compress values with their frequencies
        vals = []
        cnts = []
        cur = nums[0]
        c = 1
        for x in nums[1:]:
            if x == cur:
                c += 1
            else:
                vals.append(cur)
                cnts.append(c)
                cur = x
                c = 1
        vals.append(cur)
        cnts.append(c)

        m = len(vals)
        # Prefix sums of counts over compressed axis
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + cnts[i]

        ans = 0
        L = 0
        R = 0  # inclusive index window [L..R] where vals[j] in [vals[i]-k, vals[i]+k] as i moves

        for i in range(m):
            v = vals[i]
            # Move L to ensure vals[L] >= v - k
            while L < m and vals[L] < v - k:
                L += 1
            # Move R so that vals[R] <= v + k
            while R + 1 < m and vals[R + 1] <= v + k:
                R += 1

            in_range = pref[R + 1] - pref[L]
            freq_v = cnts[i]
            best_here = min(in_range, freq_v + numOperations)
            if best_here > ans:
                ans = best_here

            # Optional: shrink R when next i increases; but since v increases,
            # the bound v+k increases too, so we never need to move R left.

        return ans
