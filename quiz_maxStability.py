class Solution(object):
    def maxStability(self, n, edges, k):
        # Identify possible strength values for binary search boundaries
        strengths = set()
        for u, v, s, must in edges:
            strengths.add(s)
            if must == 0:
                strengths.add(s * 2)
        
        # Sort potential answers for binary search
        possible_vals = sorted(list(strengths))
        
        def can_form_mst(min_strength):
            parent = list(range(n))
            def find(i):
                if parent[i] == i: return i
                parent[i] = find(parent[i])
                return parent[i]

            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    return True
                return False

            edges_count = 0
            upgrades_used = 0
            
            # 1. Handle MUST-INCLUDE edges first
            # These cannot be upgraded, so their base strength must be >= min_strength
            for u, v, s, must in edges:
                if must == 1:
                    if s < min_strength:
                        return False # Mandatory edge fails the stability requirement
                    if union(u, v):
                        edges_count += 1
            
            # 2. Add edges that are strong enough WITHOUT upgrades
            for u, v, s, must in edges:
                if must == 0 and s >= min_strength:
                    if union(u, v):
                        edges_count += 1
            
            # 3. Add edges that need an upgrade (s < min_strength but 2s >= min_strength)
            # We only do this if we haven't reached the k limit
            for u, v, s, must in edges:
                if must == 0 and s < min_strength <= s * 2:
                    if upgrades_used < k:
                        if union(u, v):
                            edges_count += 1
                            upgrades_used += 1
            
            return edges_count == n - 1

        # Binary search on the indices of sorted possible strength values
        low, high = 0, len(possible_vals) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_mst(possible_vals[mid]):
                ans = possible_vals[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
