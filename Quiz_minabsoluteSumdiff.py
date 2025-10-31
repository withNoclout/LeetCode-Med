class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        import bisect
        MOD = 10**9 + 7
        sorted_nums1 = sorted(nums1)
        total = 0
        gain = 0

        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff
            i = bisect.bisect_left(sorted_nums1, b)
            if i < len(sorted_nums1):
                gain = max(gain, diff - abs(sorted_nums1[i] - b))
            if i > 0:
                gain = max(gain, diff - abs(sorted_nums1[i - 1] - b))

        return (total - gain) % MOD
