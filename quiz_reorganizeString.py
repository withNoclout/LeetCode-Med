import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        cnt = Counter(s)
        if max(cnt.values()) > (n + 1) // 2:
            return ""

        heap = [(-c, ch) for ch, c in cnt.items()]
        heapq.heapify(heap)

        res = []
        prev_count, prev_ch = 0, ''  # prev_count is negative when pending

        while heap:
            count, ch = heapq.heappop(heap)
            res.append(ch)
            count += 1  # since count is negative, this moves toward zero

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_ch))

            prev_count, prev_ch = count, ch

        return "".join(res)
