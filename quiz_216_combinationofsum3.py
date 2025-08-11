class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res= [] 
        path = [] 
        def dfs( start , k_left , target ) :
            if k_left == 0 and target == 0 :
                res.append(path[:] ) 
            return 
        
            for x in range( start , 10 ) :
                if x > target : 
                    break 
                path.append(x) 
                dfs( x+ 1 , k_left - 1 , target - x )
                path.pop()
        dfs(1 , k , n )
        return res
