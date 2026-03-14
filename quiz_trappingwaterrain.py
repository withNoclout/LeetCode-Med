import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
            
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the min-heap
        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
                
        for j in range(1, n - 1):
            for i in (0, m - 1):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
                
        water_trapped = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Process cells starting from the lowest boundary
        while heap:
            height, r, c = heapq.heappop(heap)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check valid, unvisited neighbors
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    
                    # If the neighbor is shorter, water is trapped
                    water_trapped += max(0, height - heightMap[nr][nc])
                    
                    # The new boundary height is the max of the current boundary or the neighbor's height
                    heapq.heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
                    
        return water_trapped
