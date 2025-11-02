class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        stack = []
        res = 0
        for i in range(n + 1):
            cur = 0 if i == n else nums[i]
            while stack and nums[stack[-1]] > cur:
                idx = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                total = prefix[right + 1] - prefix[left]
                res = max(res, total * nums[idx])
            stack.append(i)
        return res % (10**9 + 7)
