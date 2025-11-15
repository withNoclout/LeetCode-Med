import heapq

class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        heapq.heapify(nums)

        for _ in range(k):
            x = heapq.heappop(nums)
            heapq.heappush(nums, x + 1)

        prod = 1
        for x in nums:
            prod = (prod * x) % MOD
        return prod
