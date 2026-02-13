class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        # Map to store list of indices for each number
        indices = defaultdict(list)
        
        for idx, num in enumerate(nums):
            indices[num].append(idx)
            
        min_dist = float('inf')
        found = False
        
        for num in indices:
            idx_list = indices[num]
            m = len(idx_list)
            
            # We need at least 3 occurrences to form a tuple
            if m < 3:
                continue
                
            found = True
            
            # Iterate through the sorted indices and check every window of size 3.
            # We want to minimize (idx_list[x+2] - idx_list[x]) * 2
            for i in range(m - 2):
                # The distance for triplet (i, i+1, i+2) depends only on 
                # the first and last index of the triplet.
                current_dist = 2 * (idx_list[i+2] - idx_list[i])
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return min_dist if found else -1
