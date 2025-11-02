class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        res = 0
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            res = max(res, j - i - 1)
        return res
