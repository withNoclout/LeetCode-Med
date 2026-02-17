class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        # 1. Check if the total balance is sufficient to cover the debt
        if sum(balance) < 0:
            return -1
            
        n = len(balance)
        neg_index = -1
        
        # 2. Find the single index with a negative balance (the "sink")
        for i in range(n):
            if balance[i] < 0:
                neg_index = i
                break
        
        # If no index has a negative balance, 0 moves are required.
        if neg_index == -1:
            return 0
            
        needed = -balance[neg_index]
        supplies = []
        
        # 3. Collect supplies from all indices with positive balance
        for i in range(n):
            if balance[i] > 0:
                # Calculate the shortest distance on the circle between source i and sink neg_index
                dist = abs(i - neg_index)
                shortest_dist = min(dist, n - dist)
                supplies.append((shortest_dist, balance[i]))
        
        # 4. Sort supplies by distance (Greedy approach: take from closest neighbors first)
        supplies.sort(key=lambda x: x[0])
        
        moves = 0
        for dist, amount in supplies:
            # We take either the full amount available or just enough to fill the remaining need
            take = min(needed, amount)
            
            moves += take * dist
            needed -= take
            
            # If the deficit is fully covered, we stop
            if needed == 0:
                break
                
        return moves
