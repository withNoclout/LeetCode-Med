class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def maxSum(first, second):
            n = len(nums)
            max_first = curr_first = sum(nums[:first])
            max_total = curr_total = sum(nums[:first + second])
            for i in range(first + second, n):
                curr_first += nums[i - second] - nums[i - first - second]
                curr_total += nums[i] - nums[i - second]
                max_first = max(max_first, curr_first)
                max_total = max(max_total, max_first + sum(nums[i - second + 1:i + 1]))
            return max_total
        
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))
