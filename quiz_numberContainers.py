import heapq

class NumberContainers(object):

    def __init__(self):
        self.idx_to_num = {}
        self.num_to_heap = {}

    def change(self, index, number):
        if index in self.idx_to_num:
            old = self.idx_to_num[index]
        else:
            old = None

        self.idx_to_num[index] = number

        if number not in self.num_to_heap:
            self.num_to_heap[number] = []

        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number):
        if number not in self.num_to_heap:
            return -1

        heap = self.num_to_heap[number]

        while heap:
            idx = heap[0]
            if self.idx_to_num.get(idx) == number:
                return idx
            heapq.heappop(heap)

        return -1

