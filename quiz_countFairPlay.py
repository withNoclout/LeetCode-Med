class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        
        def count(target):
            res = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            return res
            
        return count(upper) - count(lower - 1)
