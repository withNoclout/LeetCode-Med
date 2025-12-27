class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        for i in range(2, -1, -1):
            diff = nums2[0] - nums1[i]
            
            p2 = 0
            for x in nums1:
                if p2 < len(nums2) and x + diff == nums2[p2]:
                    p2 += 1
            
            if p2 == len(nums2):
                return diff
        return 0
