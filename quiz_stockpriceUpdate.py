import heapq

class StockPrice(object):

    def __init__(self):
        self.prices = {}         # timestamp -> price
        self.max_heap = []       # (-price, timestamp)
        self.min_heap = []       # (price, timestamp)
        self.latest_time = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.prices[self.latest_time]

    def maximum(self):
        """
        :rtype: int
        """
        # Clean outdated entries
        while self.max_heap:
            price, time = self.max_heap[0]
            if self.prices[time] == -price:
                return -price
            heapq.heappop(self.max_heap)

    def minimum(self):
        """
        :rtype: int
        """
        # Clean outdated entries
        while self.min_heap:
            price, time = self.min_heap[0]
            if self.prices[time] == price:
                return price
            heapq.heappop(self.min_heap)
