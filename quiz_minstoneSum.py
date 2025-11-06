import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        h = [-x for x in piles]
        heapq.heapify(h)
        for _ in range(k):
            x = -heapq.heappop(h)
            x -= x // 2
            heapq.heappush(h, -x)
        return -sum(h)
