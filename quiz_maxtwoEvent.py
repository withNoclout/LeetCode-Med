import heapq

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort by start time
        events.sort(key=lambda x: x[0])

        # Min-heap by end time: (end, value)
        heap = []
        best_prev = 0   # best value of a single event that ends before current start
        ans = 0

        for s, e, v in events:
            # Pop all events that end before current starts (non-overlapping, inclusive intervals)
            while heap and heap[0][0] < s:
                end, val = heapq.heappop(heap)
                if val > best_prev:
                    best_prev = val
            # Option 1: combine current with best previous non-overlapping
            ans = max(ans, v + best_prev)
            # Option 2: take current alone
            ans = max(ans, v)
            # Push current event
            heapq.heappush(heap, (e, v))

        return ans
