class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        mod = 10**9 + 7
        sub_sums = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sub_sums.append(curr)
        sub_sums.sort()
        return sum(sub_sums[left - 1:right]) % mod
