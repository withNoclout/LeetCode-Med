from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = defaultdict(int)
        
        # Store sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                count[a + b] += 1
        
        res = 0
        # For each pair in nums3 and nums4, look for complement
        for c in nums3:
            for d in nums4:
                res += count[-(c + d)]
        
        return res
