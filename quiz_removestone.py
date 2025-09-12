class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parent = {}
        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        for x, y in stones:
            find((x, 0))
            find((y, 1))
            parent[find((x, 0))] = find((y, 1))
        return len(stones) - len({find((x, 0)) for x, y in stones} | {find((y, 1)) for x, y in stones})
