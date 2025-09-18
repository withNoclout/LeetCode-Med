class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z')+1)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
        
        for a, b in zip(s1, s2):
            union(a, b)
        
        return ''.join(find(c) for c in baseStr)
