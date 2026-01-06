class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        # Difference array to record coverage
        diff = [0] * (n + 1)
        
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
            
        current_coverage = 0
        for i in range(n):
            current_coverage += diff[i]
            # If the number is greater than the number of times it can be decremented
            if nums[i] > current_coverage:
                return False
                
        return True
