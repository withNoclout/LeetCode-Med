1231
class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        min_idx = 0
        max_idx = 0
        
        for i in range(indexDifference, len(nums)):
            check_idx = i - indexDifference
            
            if nums[check_idx] < nums[min_idx]:
                min_idx = check_idx
            if nums[check_idx] > nums[max_idx]:
                max_idx = check_idx
                
            if abs(nums[i] - nums[min_idx]) >= valueDifference:
                return [min_idx, i]
            if abs(nums[i] - nums[max_idx]) >= valueDifference:
                return [max_idx, i]
                
        return [-1, -1]
