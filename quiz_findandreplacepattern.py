class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match( w , p ) :
            m1  , m2  =  {} , {} 
            for a ,b in zip( w, p ) : 
                if m1.get( a, b)  != b or m2.get( b, a ) != a  :
                    return False 
                m1[a]  =b  
                m2[b] = a 
            return True
        
        return [ w for w in words if match( w , pattern ) ]
