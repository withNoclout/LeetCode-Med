class Solution(object):
    def maximumTripletValue(self, nums):
        res = 0
        max_diff = 0
        max_num = 0
        
        for x in nums:
            res = max(res, max_diff * x)
            max_diff = max(max_diff, max_num - x)
            max_num = max(max_num, x)
            
        return res
