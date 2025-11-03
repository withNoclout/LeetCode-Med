import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        free = [(w, i) for i, w in enumerate(servers)]  # (weight, index)
        heapq.heapify(free)
        busy = []  # (time_free, weight, index)
        res = []
        time = 0

        for i, t in enumerate(tasks):
            time = max(time, i)
            # Free up servers whose time has passed
            while busy and busy[0][0] <= time:
                tf, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            # If no free servers, jump time forward
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    tf, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))

            w, idx = heapq.heappop(free)
            res.append(idx)
            heapq.heappush(busy, (time + t, w, idx))

        return res
