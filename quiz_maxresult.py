from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        dq = deque([0])  # indices with dp decreasing

        for i in range(1, n):
            # remove indices out of window [i-k, i-1]
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            # maintain decreasing dp in deque
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            dq.append(i)

        return dp[-1]
