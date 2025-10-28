class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start = None
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break

        res = [start]
        prev = None
        while len(res) < len(adjacentPairs) + 1:
            for nxt in graph[res[-1]]:
                if nxt != prev:
                    res.append(nxt)
                    prev = res[-2]
                    break
        return res
