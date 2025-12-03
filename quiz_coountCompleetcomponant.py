class Solution(object):
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        res = 0
        
        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                nodes = 0
                edge_count = 0
                
                idx = 0
                while idx < len(q):
                    u = q[idx]
                    idx += 1
                    nodes += 1
                    edge_count += len(adj[u])
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                            
                if edge_count == nodes * (nodes - 1):
                    res += 1
        return res
