import heapq

class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.heap = []
        # push initial interval (-distance, start, end)
        # distance = distance to closest student if you seat optimally in [start,end]
        heapq.heappush(self.heap, (-(n - 1), 0, n - 1))
        self.occupied = set()

    def seat(self):
        """
        :rtype: int
        """
        while self.heap:
            dist, l, r = heapq.heappop(self.heap)
            if l > r:
                continue
            if l == 0:
                pos = 0
            elif r == self.n - 1:
                pos = self.n - 1
            else:
                pos = (l + r) // 2
            # check if pos is free
            if pos in self.occupied:
                continue
            self.occupied.add(pos)
            # push left and right intervals
            if pos - 1 >= l:
                d = (pos - 1 - l + 1) // 2
                heapq.heappush(self.heap, (-d, l, pos - 1))
            if pos + 1 <= r:
                d = (r - (pos + 1) + 1) // 2
                heapq.heappush(self.heap, (-d, pos + 1, r))
            return pos
        return -1

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.occupied.remove(p)
        # find neighbors
        left = p - 1
        while left >= 0 and left not in self.occupied:
            left -= 1
        right = p + 1
        while right < self.n and right not in self.occupied:
            right += 1
        l = left + 1
        r = right - 1
        if l <= r:
            d = 0
            if l == 0 or r == self.n - 1:
                d = r - l
            else:
                d = (r - l) // 2
            heapq.heappush(self.heap, (-d, l, r))
