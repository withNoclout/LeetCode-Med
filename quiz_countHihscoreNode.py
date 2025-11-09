import sys
sys.setrecursionlimit(1 << 20)

class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        root = 0
        for i in range(n):
            p = parents[i]
            if p == -1:
                root = i
            else:
                children[p].append(i)

        self.max_score = 0
        self.count = 0

        def dfs(u):
            # returns subtree size of u
            size = 1
            prod = 1
            for v in children[u]:
                sz = dfs(v)
                size += sz
                prod *= sz
            rest = n - size
            if rest > 0:
                prod *= rest

            if prod > self.max_score:
                self.max_score = prod
                self.count = 1
            elif prod == self.max_score:
                self.count += 1

            return size

        dfs(root)
        return self.count
