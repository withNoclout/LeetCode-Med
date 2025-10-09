class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        freq = [0] * (n + 1)
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq = freq[:n]
        nums.sort()
        freq.sort()
        mod = 10**9 + 7
        return sum(a * b for a, b in zip(nums, freq)) % mod
