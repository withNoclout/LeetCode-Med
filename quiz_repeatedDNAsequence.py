class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n= len(s)
        if n < 10 : 
            return [] 

        enc  = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
        mask = ( 1 << 20 )  -1  
        x= 0 

        for i in range(10) :
            x = ( x << 2 ) | enc[s[i]]

        seen = {x } 
        dup = set()
        res = set()

        for i in range( 10 , n ) :
            x  = (( x<< 2 ) & mask )  | enc[s[i]]
            if x in seen : 
                if x not in dup : 
                    res.add(s[i-9 : i +1 ] ) 
                    dup.add(x) 

            else : 
                seen.add(x) 

        return list(res )   
