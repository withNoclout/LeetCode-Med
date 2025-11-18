class Solution(object):
    def maximumImportance(self, n, roads):
        deg = [0] * n
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        
        deg_sorted = sorted(deg)
        
        importance = 0
        val = 1
        for d in deg_sorted:
            importance += d * val
            val += 1
        
        return importance
