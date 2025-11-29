class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()
        n = len(nums)
        
        def check(diff):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
            
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
