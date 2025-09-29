import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # sort by start time
        events.sort()
        res, day, i, n = 0, 0, 0, len(events)
        min_heap = []

        while i < n or min_heap:
            if not min_heap:
                # jump to the next event's start day
                day = events[i][0]

            # add all events starting today
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])  # push end day
                i += 1

            # remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)  # attend event with earliest end
                res += 1
                day += 1

        return res
