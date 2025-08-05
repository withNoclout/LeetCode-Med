class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = [] 

        def is_palindrome(sub) :
            return sub == sub[::-1 ] 
        
        def dfs( start , parh)  :
            if start  == len(s) : 
                res.append(path[ :  ] ) 
                return 
            for end in range( start + 1 , len(s) + 1 ) :
                if is_palindrome( s[start : end ]):
                    dfs( end  , path + [s[start : end ] ] ) 

        dfs( 0 , [] )
        return res  
