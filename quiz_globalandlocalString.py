class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        mx = -10** 9 
        n = len(nums)  
        for i in range( n - 2 ) :
            if nums[i ] > mx  : 
                mx = nums[i] 
            if mx> nums[i +  2 ] :
                return False 
        return True    
