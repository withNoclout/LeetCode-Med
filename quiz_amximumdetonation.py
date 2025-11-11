class Solution(object):
    def maximumDetonation(self, bombs):
        n = len(bombs)
        g = [[] for _ in range(n)]

        # Build directed edges: i -> j if j within i's radius
        for i in range(n):
            x1, y1, r1 = bombs[i]
            r1sq = r1 * r1
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dx = x1 - x2
                dy = y1 - y2
                if dx * dx + dy * dy <= r1sq:
                    g[i].append(j)

        def dfs(start):
            stack = [start]
            seen = {start}
            while stack:
                u = stack.pop()
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            return len(seen)

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            if ans == n:
                break
        return ans
