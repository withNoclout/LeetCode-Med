class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        left = 0 
        curr = 0 
        ans = float('inf')

        for right , x in enumerate(nums) : 
            curr += x 
            while curr >= target : 
                ans = min(ans , right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans
