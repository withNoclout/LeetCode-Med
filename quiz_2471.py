class Solution(object):
    def minimumOperations(self, root):
        q = [root]
        res = 0
        while q:
            vals = [node.val for node in q]
            
            # Find min swaps using cycle decomposition
            idx = sorted(range(len(vals)), key=lambda k: vals[k])
            visited = [False] * len(vals)
            
            for i in range(len(vals)):
                if visited[i] or idx[i] == i:
                    continue
                
                cycle = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = idx[j]
                    cycle += 1
                res += cycle - 1
                
            q = [child for node in q for child in (node.left, node.right) if child]
        return res
