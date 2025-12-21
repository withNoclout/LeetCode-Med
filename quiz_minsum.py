class Solution(object):
    def minSum(self, nums1, nums2):
        s1, z1 = sum(nums1), nums1.count(0)
        s2, z2 = sum(nums2), nums2.count(0)
        
        min_s1 = s1 + z1
        min_s2 = s2 + z2
        
        if min_s1 < min_s2 and z1 == 0:
            return -1
        if min_s2 < min_s1 and z2 == 0:
            return -1
            
        return max(min_s1, min_s2)
