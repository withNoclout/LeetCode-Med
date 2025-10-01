class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        # directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # mapping for each street type -> valid directions
        street = {
            1: [1, 3],     # left <-> right
            2: [0, 2],     # up <-> down
            3: [0, 1],     # up <-> right
            4: [1, 2],     # right <-> down
            5: [2, 3],     # down <-> left
            6: [0, 3]      # up <-> left
        }

        from collections import deque
        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            x, y = q.popleft()
            if (x, y) == (m - 1, n - 1):
                return True

            for d in street[grid[x][y]]:
                nx, ny = x + dirs[d][0], y + dirs[d][1]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # check if neighbor connects back
                    if (d ^ 2) in street[grid[nx][ny]]:
                        visited.add((nx, ny))
                        q.append((nx, ny))

        return False
