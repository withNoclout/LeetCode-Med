from collections import deque, defaultdict

class Solution(object):
    def getAncestors(self, n, edges):
        g = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])
        anc = [set() for _ in range(n)]

        while q:
            u = q.popleft()
            for v in g[u]:
                anc[v] |= anc[u]
                anc[v].add(u)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return [sorted(list(s)) for s in anc]
