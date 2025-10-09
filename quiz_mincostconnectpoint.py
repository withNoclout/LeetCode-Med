class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import heapq
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        res = 0
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            x1, y1 = points[i]
            for j in range(n):
                if j not in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))
        return res
