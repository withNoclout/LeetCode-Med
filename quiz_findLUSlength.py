class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_sunseq( a, b ) :
            i = j = 0 
            while i < len(a) and j < len(b)  : 
                if a[i] == b[j]:
                    i += 1
                j+= 1 
            return i == len(a) 
        
        strs.sort(key=len, reverse=True)    

        for i , s in enumerate(strs) :
            if all( not is_sunseq(s, strs[j]) for j in range(len(strs)) if j != i):
                return len(s)
        return -1
