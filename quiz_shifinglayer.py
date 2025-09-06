class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

        n = len(s)

        total = sum( shifts ) & 26 
        res = [] 

        for i , ch in enumerate(s) :
            x = (ord(ch) )  - 97 + total % 26 
            res.append( chr( x+ 97 ) ) 
            total = ( total - shifts[i] ) % 26
        return ''.join(res)   
