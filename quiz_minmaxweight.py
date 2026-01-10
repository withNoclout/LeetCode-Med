from collections import deque

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minMaxWeight(self, n, edges, threshold):
        # 1. สร้าง Adjacency List แบบย้อนกลับ (v -> u)
        adj = [[] for _ in range(n)]
        max_edge_w = 0
        for u, v, w in edges:
            adj[v].append((u, w))
            if w > max_edge_w:
                max_edge_w = w
        
        # 2. ฟังก์ชันตรวจสอบว่าด้วย weight limit นี้ จะไปถึงทุกโหนดได้ไหม
        def can_reach_all(limit):
            visited = [False] * n
            visited[0] = True
            queue = deque([0])
            visited_count = 1
            
            while queue:
                curr = queue.popleft()
                for neighbor, weight in adj[curr]:
                    if not visited[neighbor] and weight <= limit:
                        visited[neighbor] = True
                        visited_count += 1
                        queue.append(neighbor)
            return visited_count == n

        # 3. Binary Search หาค่า weight ที่น้อยที่สุด
        low, high = 1, max_edge_w
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_all(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result
