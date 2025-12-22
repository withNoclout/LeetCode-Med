class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        memo = {}
        
        def dp(v):
            if v <= y:
                return y - v
            if v in memo:
                return memo[v]
            
            # Option 1: Just decrement to y
            res = v - y
            
            # Option 2: Go to nearest multiple of 11, then divide
            res = min(res, v % 11 + 1 + dp(v // 11))
            res = min(res, (11 - v % 11) + 1 + dp(v // 11 + 1))
            
            # Option 3: Go to nearest multiple of 5, then divide
            res = min(res, v % 5 + 1 + dp(v // 5))
            res = min(res, (5 - v % 5) + 1 + dp(v // 5 + 1))
            
            memo[v] = res
            return res
            
        return dp(x)
