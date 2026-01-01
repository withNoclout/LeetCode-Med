class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        n = len(nums)
        
        while cur < n - 1:
            nxt = cur + 1
            while nxt < n - 1 and nums[nxt] <= nums[cur]:
                nxt += 1
                
            ans += (nxt - cur) * nums[cur]
            cur = nxt
            
        return ans
