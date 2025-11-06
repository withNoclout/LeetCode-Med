class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        Offline DSU for queries of the form [u, v, limit]:
        return 1 if there exists a path between u and v using only edges with weight < limit, else 0.
        :type c: int
        :type connections: List[List[int]]  # [u, v, w]
        :type queries: List[List[int]]      # [u, v, limit]
        :rtype: List[int]                   # 0/1 per query
        """
        parent = list(range(c))
        size = [1] * c

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Sort edges by weight
        connections.sort(key=lambda e: e[2])

        # Prepare queries with original index, sort by limit
        indexed = [(lim, u, v, i) for i, (u, v, lim) in enumerate(queries)]
        indexed.sort()

        res = [0] * len(queries)
        ei = 0  # edge index

        for lim, u, v, qi in indexed:
            # add all edges with weight < lim
            while ei < len(connections) and connections[ei][2] < lim:
                union(connections[ei][0], connections[ei][1])
                ei += 1
            res[qi] = 1 if find(u) == find(v) else 0

        return res
