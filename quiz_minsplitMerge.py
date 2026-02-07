class Solution(object):
    def minSplitMerge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # We assume the total sums must be equal for a solution to exist
        if sum(nums1) != sum(nums2):
            return -1
            
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        val1, val2 = 0, 0
        matches = 0
        
        while i < n or j < m:
            # If current running sums are empty, initialize them
            if val1 == 0 and i < n:
                val1 = nums1[i]
                i += 1
            if val2 == 0 and j < m:
                val2 = nums2[j]
                j += 1
                
            # If equal, we found a matching segment boundary
            if val1 == val2:
                matches += 1
                val1, val2 = 0, 0
            # If val1 is smaller, we need to merge more into nums1 side
            elif val1 < val2:
                if i < n:
                    val1 += nums1[i]
                    i += 1
            # If val1 is larger, we need to merge more into nums2 side
            else:
                if j < m:
                    val2 += nums2[j]
                    j += 1
                    
        # Total operations = (merges needed for nums1) + (splits/merges needed for nums2)
        # Merges in nums1 = n - matches
        # Merges in nums2 = m - matches
        return (n - matches) + (m - matches)
