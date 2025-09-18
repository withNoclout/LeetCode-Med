import heapq
from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = Counter(barcodes)
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        res = []
        prev_freq, prev_num = 0, None
        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_num))
            freq += 1  # since freq is negative
            prev_freq, prev_num = freq, num
        return res
