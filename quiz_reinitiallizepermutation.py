class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        pos = 1 
        steps = 0  
        while True : 
            if pos % 2 == 0 : 
                pos = pos // 2 
            else: 
                pos = n // 2 + pos // 2 
            steps += 1 

            if pos == 1 : 
                return steps 
            
