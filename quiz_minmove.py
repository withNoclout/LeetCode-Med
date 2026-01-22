class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - len(nums) * min(nums)



from collections import deque, defaultdict

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        # 1. Map all portal locations for O(1) access
        portals = defaultdict(list)
        for r in range(m):
            for c in range(n):
                char = matrix[r][c]
                if 'A' <= char <= 'Z':
                    portals[char].append((r, c))
        
        # 2. Initialize 0-1 BFS
        # dist[r][c] stores the minimum moves to reach cell (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque stores (r, c). 
        # Front: 0-cost moves (teleport). Back: 1-cost moves (walk).
        q = deque([(0, 0)])
        
        while q:
            r, c = q.popleft()
            d = dist[r][c]
            
            # Target reached
            if r == m - 1 and c == n - 1:
                return d
            
            # Option 1: Teleport (Cost 0)
            # If current cell has a portal and we haven't used this letter yet
            char = matrix[r][c]
            if char in portals:
                for tr, tc in portals[char]:
                    if d < dist[tr][tc]:
                        dist[tr][tc] = d
                        q.appendleft((tr, tc)) # Push to front (priority)
                
                # Important: Remove this letter from map to ensure 
                # we don't process this portal group again (avoid infinite loops/redundancy)
                del portals[char]
            
            # Option 2: Walk Adjacent (Cost 1)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#':
                    if d + 1 < dist[nr][nc]:
                        dist[nr][nc] = d + 1
                        q.append((nr, nc)) # Push to back
                        
        return -1
