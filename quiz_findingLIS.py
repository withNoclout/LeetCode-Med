class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        length = [1] * n   # LIS length ending at i
        count = [1] * n    # number of LIS ending at i

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]      # reset count
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]     # add ways

        longest = max(length)
        return sum(c for l, c in zip(length, count) if l == longest)
