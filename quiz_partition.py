class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        count = 1
        start = nums[0]

        for x in nums:
            if x - start > k:
                count += 1
                start = x

        return count
