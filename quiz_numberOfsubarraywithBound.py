class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def count(bound):
            ans = cur = 0
            for x in nums:
                cur = 0 if x > bound else cur + 1
                ans += cur
            return ans

        return count(right) - count(left - 1)
