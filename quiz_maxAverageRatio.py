import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def gain(p, t):
            return (p + 1.0) / (t + 1.0) - (p * 1.0) / t

        # max-heap by gain -> use negative for heapq
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        n = len(heap)
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p * 1.0 / t
        return total / n
