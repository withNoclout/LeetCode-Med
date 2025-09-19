class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = { c: i for i  ,c  in enumerate(s ) } 
        stack = [] 
        seen = set() 

        for i , c in enumerate(s)  :
            if c not in seen : 
                continue 
            while stack and c < stack[-1] and i < last[stack[-1]]  :
                seen.remove(stack.pop()) 
            stack,append(c)  
            seen.add(c) 
        return ''.join(stack)
