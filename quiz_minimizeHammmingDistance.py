class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)

        # Build DSU for all swappable indices
        for a, b in allowedSwaps:
            union(a, b)

        # Group indices by connected component
        groups = {}
        for i in range(len(source)):
            root = find(i)
            groups.setdefault(root, []).append(i)

        res = 0
        # For each group, compare value frequencies
        from collections import Counter
        for idxs in groups.values():
            s_count = Counter(source[i] for i in idxs)
            t_count = Counter(target[i] for i in idxs)
            # Count mismatches
            for val in s_count:
                common = min(s_count[val], t_count.get(val, 0))
                s_count[val] -= common
            res += sum(s_count.values())
        return res
