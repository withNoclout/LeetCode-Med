import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n = len(apples)
        heap = []  # (expire_day, count)
        eaten = 0
        day = 0

        while day < n or heap:
            # Add today's apples with their expiry
            if day < n and apples[day] > 0 and days[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            # Remove expired batches
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # Eat one apple from the batch that expires soonest
            if heap:
                exp, cnt = heapq.heappop(heap)
                eaten += 1
                if cnt - 1 > 0:
                    heapq.heappush(heap, (exp, cnt - 1))

            day += 1

        return eaten
