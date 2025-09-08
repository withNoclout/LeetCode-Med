# ...existing code...
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque

        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        color = [0] * (n + 1)  # 0 = uncolored, 1 and -1 are the two groups

        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            if not adj[i]:
                color[i] = 1
                continue
            q = deque([i])
            color[i] = 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
# ...existing
