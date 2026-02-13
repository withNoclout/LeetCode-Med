class Solution(object):
    def countStableSubarrays(self, capacity):
        """
        :type capacity: List[int]
        :rtype: int
        """
        n = len(capacity)
        if n < 3:
            return 0
            
        # Build prefix sum array
        # P[i] represents sum of capacity[0...i-1]
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + capacity[i]
            
        # Dictionary to store counts of valid left indices 'l'
        # Structure: { value : { prefix_sum : count } }
        from collections import defaultdict
        seen = defaultdict(lambda: defaultdict(int))
        
        ans = 0
        
        # Iterate through 'r' starting from index 2 (minimum length 3)
        for r in range(2, n):
            # Before processing r, add the new valid 'l' index (r-2) to the map.
            # This ensures we only match with l such that r - l >= 2 (length >= 3).
            l_idx = r - 2
            val_l = capacity[l_idx]
            p_l = P[l_idx]
            
            seen[val_l][p_l] += 1
            
            # Check for valid stable subarrays ending at r
            val_r = capacity[r]
            
            # Derived condition: P[l] = P[r] - 2 * val
            # We look for previously seen l's that have the same value (val_r)
            # and the specific prefix sum needed.
            target_p_l = P[r] - 2 * val_r
            
            if val_r in seen:
                ans += seen[val_r][target_p_l]
                
        return ans
