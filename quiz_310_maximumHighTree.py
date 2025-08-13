class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        graph = defaultdict(set ) 
        deg = [0] *n 
        for a , b in edges : 
            graph[a].add(b) 
            graph[b].add(a) 
            deg[a] += 1 
            deg[b] += 1 

        leaves = deque(i for i in range(n) if deg[i] ==1 ) 
        remaining = n 

        while remaining >2 : 
            size = len(leaves ) 
            remaining -= size 
            for _ in range(size) :
                leaf = leaves.popleft()
                for nei in list(graph[leaf] ):
                    graph[nei].remove(leaf) 
                    deg[nei]  -= 1 
                    if deg[nei] == 1:
                        leaves.append(nei)
                graph[leaf].clear()
        return list(leaves)
