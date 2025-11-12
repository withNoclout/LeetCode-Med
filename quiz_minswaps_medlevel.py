class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        k = sum(nums)
        if k <= 1 or k == n:
            return 0

        max_ones = 0
        curr = 0
        left = 0

        # Slide a window of size k over the circular array using two passes
        for right in range(2 * n):
            curr += nums[right % n]
            if right - left + 1 > k:
                curr -= nums[left % n]
                left += 1
            if right - left + 1 == k and left < n:
                max_ones = max(max_ones, curr)
            if left >= n:
                break

        return k - max_ones
