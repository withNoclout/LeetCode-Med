class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        import collections
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        parent = {0: -1}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in parent:
                    parent[v] = u
                    stack.append(v)
                    
        bob_time = {}
        curr, time = bob, 0
        while curr != -1:
            bob_time[curr] = time
            curr = parent[curr]
            time += 1
            
        res = float('-inf')
        stack = [(0, -1, 0, 0)] 
        
        while stack:
            u, p, t, curr_sum = stack.pop()
            
            val = amount[u]
            if u in bob_time:
                if bob_time[u] < t: val = 0
                elif bob_time[u] == t: val //= 2
            
            curr_sum += val
            
            is_leaf = True
            for v in graph[u]:
                if v != p:
                    is_leaf = False
                    stack.append((v, u, t + 1, curr_sum))
            
            if is_leaf:
                res = max(res, curr_sum)
                
        return res
