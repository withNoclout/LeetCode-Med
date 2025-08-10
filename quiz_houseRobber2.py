class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        if n == 1 : 
            return nums[0]
        
        def rob_line( arr ) :
            rob1 = rob2 =  0 
            for x in arr : 
                rob1, rob2 = rob2, max(rob1 + x, rob2)
            return rob2     
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
