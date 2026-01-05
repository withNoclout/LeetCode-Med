class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        maximumHeight.sort(reverse=True)
        total = 0
        curr = float('inf')
        
        for h in maximumHeight:
            assign = min(h, curr - 1)
            if assign <= 0:
                return -1
            total += assign
            curr = assign
            
        return total
