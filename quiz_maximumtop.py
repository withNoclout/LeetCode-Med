class Solution(object):
    def maximumTop(self, nums, k):
        n = len(nums)
        if k == 0:
            return nums[0]
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]

        ans = float('-inf')
        # Option 1: after k moves, top is some element among first k-1 removed elements
        if k - 1 > 0:
            ans = max(ans, max(nums[:k-1]))
        # Option 2: after k moves, top is nums[k] (if exists)
        if k < n:
            ans = max(ans, nums[k])
        # If k >= n, Option 1 already considered all elements (since k-1 >= n)
        return ans

