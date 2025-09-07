class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Greedy: try to beat each nums2 element (from largest to smallest) with the largest possible nums1
        sorted_a = sorted(nums1)
        result = [0] * len(nums2)
        # Sort nums2 with indices descending by value
        b_with_idx = sorted([(v, i) for i, v in enumerate(nums2)], reverse=True)
        lo, hi = 0, len(sorted_a) - 1
        for val_b, idx in b_with_idx:
            if sorted_a[hi] > val_b:
                result[idx] = sorted_a[hi]
                hi -= 1
            else:
                result[idx] = sorted_a[lo]
                lo += 1
        return
