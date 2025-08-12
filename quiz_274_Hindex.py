class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h= 0 
        for i , c in enumerate(citations ) :
            if c >= i : 
                h= i 
            else : 
                break 
        return h 
