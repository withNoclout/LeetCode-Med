class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        for a, b in pairs:
            union(a, b)

        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        res = list(s)
        for idxs in groups.values():
            chars = [s[i] for i in idxs]
            idxs.sort()
            chars.sort()
            for i, ch in zip(idxs, chars):
                res[i] = ch

        return "".join(res)

