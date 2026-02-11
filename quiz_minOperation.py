class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        target = nums2[-1]
        
        # Base cost: 1 operation for the inevitable "Append"
        ans = 1
        
        min_dist_to_target = float('inf')
        is_covered = False
        
        for i in range(n):
            curr = nums1[i]
            goal = nums2[i]
            
            # Add the cost to transform nums1[i] to nums2[i]
            ans += abs(curr - goal)
            
            # Check if the target value lies within the path from curr to goal
            low, high = min(curr, goal), max(curr, goal)
            
            if low <= target <= high:
                is_covered = True
            else:
                # Calculate strictly how far the target is from the interval [low, high]
                # We can "branch off" from either endpoint
                dist = min(abs(curr - target), abs(goal - target))
                min_dist_to_target = min(min_dist_to_target, dist)
                
        # If the target value was never strictly "on the way" of any transformation,
        # we add the minimum cost to reach it from the closest point visited.
        if not is_covered:
            ans += min_dist_to_target
            
        return ans
