from collections import deque, defaultdict

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency lists for red and blue edges
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        # result array, -1 means unreachable
        res = [-1] * n
        # visited[node][color]: color 0=red, 1=blue
        visited = [[False, False] for _ in range(n)]
        # queue: (node, steps, last_color)
        # last_color: 0=red, 1=blue
        q = deque()
        q.append((0, 0, -1))  # start from node 0, no color yet
        visited[0][0] = visited[0][1] = True
        res[0] = 0

        while q:
            node, steps, last_color = q.popleft()
            # Try both colors
            for color, adj in enumerate([red_adj, blue_adj]):
                if color == last_color:
                    continue  #
