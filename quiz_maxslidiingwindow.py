from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        
        res = []
        dq = deque() # Stores indices
        
        for i in range(len(nums)):
            # 1. Remove indices of elements smaller than the current element
            # because they will never be the maximum again.
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            # 2. Add current element's index to the back
            dq.append(i)
            
            # 3. Remove the front index if it's out of the current window's range
            if dq[0] <= i - k:
                dq.popleft()
            
            # 4. Once the first window is fully formed (i >= k-1),
            # the front of the deque is the max for the current window.
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res
