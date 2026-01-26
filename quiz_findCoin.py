class Solution(object):
    def findCoins(self, numWays):
        """
        :type numWays: List[int]
        :rtype: List[int]
        """
        # Custom GCD module as required by your rules
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        n = len(numWays)
        coins = []
        
        # current_ways represents the number of ways to make change 
        # using only the coins we have discovered SO FAR.
        # Base case: 1 way to make amount 0 (empty set).
        current_ways = [0] * (n + 1)
        current_ways[0] = 1
        
        # We iterate through amounts from 1 to n
        for i in range(1, n + 1):
            target_val = numWays[i-1] # numWays[0] corresponds to amount 1
            
            # If our current coins can't explain the number of ways to make amount 'i',
            # the difference MUST be due to a new coin of value 'i' being introduced.
            if current_ways[i] < target_val:
                # We found a new coin of value 'i'
                # The count of this coin is the difference / ways[0] (which is 1)
                # But typically distinct coins appear once. If duplicates allowed, 
                # we'd add 'i' multiple times. Assuming distinct based on standard LC types.
                # Actually, standard problem implies we just append 'i'.
                
                # Check how many times we need to add coin 'i'
                # Usually standard constraint implies distinct coins, but let's handle count.
                count = target_val - current_ways[i]
                
                for _ in range(count):
                    coins.append(i)
                    
                    # Update current_ways to include the effect of this new coin
                    # classic unbounded knapsack update
                    for j in range(i, n + 1):
                        current_ways[j] += current_ways[j - i]
                        
        return coins
