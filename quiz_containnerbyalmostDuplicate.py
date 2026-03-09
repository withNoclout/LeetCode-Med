class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0: return False
        buckets = {}
        # Bucket size is valueDiff + 1 to handle valueDiff = 0
        w = valueDiff + 1
        
        for i in range(len(nums)):
            # Normalize number into a bucket index
            m = nums[i] // w
            
            # 1. Check if the current bucket already has a number
            if m in buckets:
                return True
            
            # 2. Check the adjacent bucket to the left
            if (m - 1) in buckets and abs(nums[i] - buckets[m - 1]) < w:
                return True
            
            # 3. Check the adjacent bucket to the right
            if (m + 1) in buckets and abs(nums[i] - buckets[m + 1]) < w:
                return True
            
            # Add current number to its bucket
            buckets[m] = nums[i]
            
            # 4. Maintain the sliding window of size indexDiff
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // w]
                
        return False
