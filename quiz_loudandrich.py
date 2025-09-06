class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        # graph: edges from person -> people richer than them
        g = [[] for _ in range(n)]
        for u, v in richer:  # u richer than v
            g[v].append(u)

        ans = [-1] * n  # ans[i] = index of least quiet among {i and richer-than-i}

        def dfs(i):
            if ans[i] != -1:
                return ans[i]
            best = i
            for j in g[i]:
                cand = dfs(j)
                if quiet[cand] < quiet[best]:
                    best = cand
            ans[i] = best
            return best

        for i in range(n):
            dfs(i)
        return ans
