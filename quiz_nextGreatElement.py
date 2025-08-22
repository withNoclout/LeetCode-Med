class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums ) 
        res = [-1 ] * n  
        stack = [] 

        for i in range( 2* n ) :
            while stack and nums[stack[-1] ] < nums[i% n ] : 
                res[stack.pop() ] = nums[i% n]
            if i < n : 
                stack.append(i % n)

        return res 
