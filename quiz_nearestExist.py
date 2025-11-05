class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visited = set([(entrance[0], entrance[1])])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            i, j, dist = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.' and (ni, nj) not in visited:
                    if ni == 0 or ni == m-1 or nj == 0 or nj == n-1:
                        return dist + 1
                    visited.add((ni, nj))
                    q.append((ni, nj, dist + 1))
        return -1
