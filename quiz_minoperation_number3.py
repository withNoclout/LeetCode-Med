class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0

        # Ensure s1 < s2 so we always try to increase nums1 or decrease nums2
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        diff = s2 - s1  # positive
        # counts of possible gains [1..5]
        gains = [0] * 6
        for x in nums1:
            gains[6 - x] += 1  # how much we can increase x (up to 6)
        for x in nums2:
            gains[x - 1] += 1  # how much we can decrease x (down to 1)

        ops = 0
        for d in range(5, 0, -1):
            if diff <= 0:
                break
            take = min(gains[d], (diff + d - 1) // d)
            ops += take
            diff -= take * d

        return ops if diff <= 0 else -1
