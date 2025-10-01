import heapq

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # Max heap: store counts as negative for heapq
        max_heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        res = []
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            # If last two characters are same as char1, we must pick another char
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not max_heap:  # no alternative → stop
                    break
                count2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                count2 += 1  # use one instance
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count1, char1))  # push back char1
            else:
                res.append(char1)
                count1 += 1  # use one instance
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, char1))

        return "".join(res)
