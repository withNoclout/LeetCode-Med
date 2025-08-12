class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7

        bases = []
        i = 1 
        while True : 
            p = i ** x 
            if p > n : 
                break 
            bases.append(p)
            i += 1 

        memo = {}
        def dfs( idx , total ) :
            if total == n :
                return 1 
            
            if idx == len(bases) or total > n : 
                return 0 
            key = ( idx , total ) 

            if key in memo :
                return memo[key] 
            
            take = dfs( idx + 1, total - bases[idx] ) 
            skip = dfs( idx + 1 , total ) 

            memo[key ] = ( take + skip )  % MOD 
            return memo[key] 
        
        return dfs( 0 , n ) 
