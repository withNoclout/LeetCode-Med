class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [''] 
        for ch in s : 
            if ch.isalpha() :
                res = [ p + ch.lower() for p in res ] + [ p + ch.upper() for p in res ]

            else: 
                res=  [ p+ ch for p in res ] 

        return res 
        
