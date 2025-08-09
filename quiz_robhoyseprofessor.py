class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 = rob2 = 0 
        for x in nums : 
            rob1, rob2 = rob2, max(rob2, rob1 + x)
        return rob2
    

