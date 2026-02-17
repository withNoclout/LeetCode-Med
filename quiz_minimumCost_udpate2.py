class Solution(object):
    def minimumCost(self, s, t, flipCost, swapCost, crossCost):
        """
        :type s: str
        :type t: str
        :type flipCost: int
        :type swapCost: int
        :type crossCost: int
        :rtype: int
        """
        cnt01 = 0
        cnt10 = 0
        
        # 1. Count the two types of mismatches
        for i in range(len(s)):
            if s[i] != t[i]:
                if s[i] == '0':
                    cnt01 += 1
                else:
                    cnt10 += 1
                    
        total_cost = 0
        
        # 2. Pair up mismatches of different types (01 and 10)
        # We can fix one '01' and one '10' together using a single Swap
        matched_pairs = min(cnt01, cnt10)
        total_cost += matched_pairs * min(swapCost, 2 * flipCost)
        
        # 3. Handle remaining mismatches (all of the same type)
        remaining = abs(cnt01 - cnt10)
        
        # Group them into pairs of (01, 01) or (10, 10)
        same_pairs = remaining // 2
        
        # To fix two identical errors:
        # Option A: Flip both (2 * flipCost)
        # Option B: Cross-swap one to change type, then Swap (crossCost + swapCost)
        total_cost += same_pairs * min(crossCost + swapCost, 2 * flipCost)
        
        # 4. Handle the last single error if one exists
        if remaining % 2 == 1:
            total_cost += flipCost
            
        return total_cost
