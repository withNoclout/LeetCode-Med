class Solution(object):
    def maxScoreIndices(self, nums):
        n = len(nums)
        ones_right = sum(nums)
        zeros_left = 0

        best = -1
        res = []

        for i in range(n + 1):
            score = zeros_left + ones_right
            if score > best:
                best = score
                res = [i]
            elif score == best:
                res.append(i)

            if i < n:
                if nums[i] == 0:
                    zeros_left += 1
                else:
                    ones_right -= 1

        return res
