class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def ways(s ) :
            if s in memo :
                return memo[s]  
            
            res = []
            for i ,ch in enumerate(s) :
                if ch in '+-*' :
                    left = ways(s[:i])
                    right = ways(s[i+1:])
                    for a in left:
                        for b in right :
                            if ch== '+' :
                                res.append(a+b) 
                            elif ch == '-' :
                                res.append(a-b)
                            else : 
                                res.append(a*b) 

            if not res :
                res = [int(s)]  
            memo[s] = res 
            return res 
        return ways(expression)
