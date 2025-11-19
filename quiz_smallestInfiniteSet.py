import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1
        self.added = set()
        self.heap = []

    def popSmallest(self):
        if self.heap and self.heap[0] < self.curr:
            x = heapq.heappop(self.heap)
            self.added.remove(x)
            return x
        x = self.curr
        self.curr += 1
        return x

    def addBack(self, num):
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
