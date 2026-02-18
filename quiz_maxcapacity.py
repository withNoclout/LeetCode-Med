import bisect

class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        # Combine costs and capacity into a list of tuples (cost, capacity)
        # Sort based on cost to enable binary search
        items = sorted(zip(costs, capacity))
        
        # Extract just the costs for binary searching
        sorted_costs = [x[0] for x in items]
        n = len(items)
        
        if n == 0:
            return 0
            
        # Precompute prefix maximum capacity
        # prefix_max[k] will hold the max capacity among the first k+1 items (indices 0 to k)
        prefix_max = [0] * n
        prefix_max[0] = items[0][1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], items[i][1])
            
        max_total_cap = 0
        
        # Iterate through every machine considering it as the "heavier" or "second" item in a pair
        for i in range(n):
            current_cost, current_cap = items[i]
            
            # Case 1: Select exactly one machine (this one)
            if current_cost < budget:
                max_total_cap = max(max_total_cap, current_cap)
            
            # Case 2: Select two distinct machines
            # We need to find a partner j such that: items[j].cost < budget - current_cost
            remaining_budget = budget - current_cost
            
            # Binary search to find the insertion point for remaining_budget
            # bisect_left gives the first index where value >= remaining_budget
            # All indices strictly before this index satisfy the condition < remaining_budget
            idx = bisect.bisect_left(sorted_costs, remaining_budget)
            
            # We must choose a partner strictly before 'i' to ensure:
            # 1. Distinctness (j != i)
            # 2. We don't double count pairs (we pair j with i where j < i)
            # The valid index range for the partner is [0, min(i, idx) - 1]
            valid_limit = min(i, idx) - 1
            
            if valid_limit >= 0:
                # The best partner is the one with max capacity in the valid range
                best_partner_cap = prefix_max[valid_limit]
                max_total_cap = max(max_total_cap, current_cap + best_partner_cap)
                
        return max_total_cap
