from collections import Counter
import heapq

class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        cnt = Counter(s)
        # max-heap of characters by lexicographic order (use negative ord)
        heap = [(-ord(ch), ch, cnt[ch]) for ch in cnt]
        heapq.heapify(heap)

        res = []
        while heap:
            _, ch, freq = heapq.heappop(heap)
            use = min(freq, repeatLimit)
            res.append(ch * use)
            freq -= use
            if freq > 0 and heap:
                # use next smaller character once to break the sequence
                _, ch2, freq2 = heapq.heappop(heap)
                res.append(ch2)
                freq2 -= 1
                if freq2 > 0:
                    heapq.heappush(heap, (-ord(ch2), ch2, freq2))
                heapq.heappush(heap, (-ord(ch), ch, freq))
            # if no smaller char available, stop
        return ''.join(res)
