class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def countCells(self, grid, pattern):
        """
        :type grid: List[List[str]]
        :type pattern: str
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        total_cells = m * n
        
        # 1. Construct the flattened Horizontal String (row by row)
        h_str_list = []
        for r in range(m):
            h_str_list.append("".join(grid[r]))
        h_str = "".join(h_str_list)
        
        # 2. Construct the flattened Vertical String (col by col)
        v_str_list = []
        for c in range(n):
            col_chars = [grid[r][c] for r in range(m)]
            v_str_list.append("".join(col_chars))
        v_str = "".join(v_str_list)
        
        # 3. Get covered indices for both directions
        # h_covered[k] is True if the cell at flat index k (row-major) is part of a horizontal match
        h_covered = self._get_covered_indices(h_str, pattern)
        
        # v_covered[k] is True if the cell at flat index k (col-major) is part of a vertical match
        v_covered = self._get_covered_indices(v_str, pattern)
        
        count = 0
        
        # 4. Count intersections
        # Iterate through every cell in the grid (using row-major index k)
        for k in range(total_cells):
            if h_covered[k]:
                # Map row-major index k to (r, c)
                r = k // n
                c = k % n
                
                # Convert (r, c) to col-major index for vertical check
                # Col-major index = c * m + r
                v_idx = c * m + r
                
                if v_covered[v_idx]:
                    count += 1
                    
        return count

    def _get_covered_indices(self, text, pattern):
        """
        Returns a boolean array where arr[i] is True if text[i] is part of any occurrence of pattern.
        """
        n = len(text)
        p = len(pattern)
        if p > n:
            return [False] * n
            
        # KMP Step 1: Build PI table (LPS array)
        pi = [0] * p
        j = 0
        for i in range(1, p):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
            
        # KMP Step 2: Find all start indices of matches
        matches_start = []
        j = 0
        for i, char in enumerate(text):
            while j > 0 and char != pattern[j]:
                j = pi[j-1]
            if char == pattern[j]:
                j += 1
            if j == p:
                matches_start.append(i - p + 1)
                j = pi[j-1]
        
        # Step 3: Use Difference Array to mark covered ranges in O(N)
        diff = [0] * (n + 1)
        for start in matches_start:
            diff[start] += 1
            if start + p <= n:
                diff[start + p] -= 1
                
        is_covered = [False] * n
        current_overlap = 0
        for i in range(n):
            current_overlap += diff[i]
            if current_overlap > 0:
                is_covered[i] = True
                
        return is_covered
