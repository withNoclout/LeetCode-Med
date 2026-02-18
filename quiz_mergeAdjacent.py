class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for x in nums:
            # While the stack is not empty and the current element equals the top of the stack
            while stack and stack[-1] == x:
                # Pop the top element
                top = stack.pop()
                # Merge: Update x to be the sum
                x = top + x
                # Continue the loop to check if the NEW x matches the NEW top
            
            # Once x no longer matches the top (or stack is empty), push it
            stack.append(x)
            
        return stack
