class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        i_min = nums.index(min(nums))
        i_max = nums.index(max(nums))
        l, r = min(i_min, i_max), max(i_min, i_max)
        return min(r + 1, n - l, (l + 1) + (n - r))
