class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        n = len(tasks)
        tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        res = []
        h = []
        time = 0
        i = 0

        while i < n or h:
            if not h and time < tasks[i][0]:
                time = tasks[i][0]
            while i < n and tasks[i][0] <= time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                pt, idx = heapq.heappop(h)
                time += pt
                res.append(idx)
        return res
