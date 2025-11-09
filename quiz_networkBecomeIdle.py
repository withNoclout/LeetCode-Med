from collections import deque

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # BFS from server 0 to get shortest hop distances
        dist = [-1] * n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        ans = 0
        for i in range(1, n):
            rtt = 2 * dist[i]
            if patience[i] >= rtt:
                last_send = 0
            else:
                last_send = ((rtt - 1) // patience[i]) * patience[i]
            idle_time = last_send + rtt + 1
            if idle_time > ans:
                ans = idle_time
        return ans
