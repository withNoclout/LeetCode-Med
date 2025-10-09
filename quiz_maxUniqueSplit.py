class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = set()
        self.res = 0 

        def backtrack(start ) :
            if start == len(s)  :
                self.res = max( self.res , len(used ) ) 
                return 
            
            for end in range( start + 1 , len(s) + 1 ) :
                sub = s[start : end ] 
                if sub not in used : 
                    used.add(sub) 
                    backtrack(end ) 
                    used.remove(sub) 

        backtrack(0)
        return self.res 
