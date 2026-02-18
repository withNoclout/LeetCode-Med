from collections import deque, defaultdict

class Solution(object):
    def specialNodes(self, n, edges, x, y, z):
        """
        :type n: int
        :type edges: List[List[int]]
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        # 1. Build the graph (Adjacency List)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. Helper function to compute distances from a source node to all others
        def get_distances(start_node):
            dists = [-1] * n
            dists[start_node] = 0
            queue = deque([start_node])
            
            while queue:
                curr = queue.popleft()
                current_dist = dists[curr]
                
                for neighbor in graph[curr]:
                    if dists[neighbor] == -1:
                        dists[neighbor] = current_dist + 1
                        queue.append(neighbor)
            return dists
            
        # 3. Compute distances from the three target nodes
        dist_x = get_distances(x)
        dist_y = get_distances(y)
        dist_z = get_distances(z)
        
        count = 0
        
        # 4. Check the condition for every node in the tree
        for u in range(n):
            # Get the three distances
            d1 = dist_x[u]
            d2 = dist_y[u]
            d3 = dist_z[u]
            
            # Sort them to identify a, b, c such that a <= b <= c
            sides = sorted([d1, d2, d3])
            a, b, c = sides[0], sides[1], sides[2]
            
            # Check Pythagorean theorem: a^2 + b^2 == c^2
            # Note: Example 1 implies 0-length distances are valid (e.g., node 1 has dists 0, 2, 2)
            if a*a + b*b == c*c:
                count += 1
                
        return count
