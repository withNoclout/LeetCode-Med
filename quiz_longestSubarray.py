from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_dq, min_dq = deque(), deque()  # decreasing for max, increasing for min
        left = 0
        res = 0

        for right, num in enumerate(nums):
            # Maintain decreasing deque for max
            while max_dq and num > max_dq[-1]:
                max_dq.pop()
            max_dq.append(num)

            # Maintain increasing deque for min
            while min_dq and num < min_dq[-1]:
                min_dq.pop()
            min_dq.append(num)

            # If current window invalid, shrink from left
            while max_dq[0] - min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res
