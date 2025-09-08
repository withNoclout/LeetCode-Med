class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        max_r = 0 
        for l , r in queries : 
            if r > max_r : 
                max_r = r 

        powers = [1 ] 
        while powers[-1] <= max_r : 
            nxt = powers[-1] * 4 
            powers.append(nxt ) 

        def G(n ) :
            if n <= 0 : 
                return 0 
            
            total = 0 
            for k in range( len(power ) - 1 ) :
                if powers[k] > n  :
                    break 

                hi = min(n , powers[k+1 ]- 1  )  
                cnt = hi - powers[k ]  + 1 

                if cnt  > 0 :
                    total += k * cnt  

            return total 
        
        def F(n) :
            if n <= 0  : 
                return 0 
            return n + G(n) 
        
        ans  = 0 
        for l , r in queries : 
            segment_sum  = F(r ) - F(l - 1 )
            ans += (segment_sum + 1) // 2

        return ans 
