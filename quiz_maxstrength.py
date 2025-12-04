class Solution(object):
    def maxStrength(self, nums):
        if len(nums) == 1:
            return nums[0]
            
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        # If there are no positive numbers and at most 1 negative number,
        # the remaining numbers must be zeros (since len > 1).
        # In this case, the max strength is 0 (e.g., [-5, 0] -> 0, [0, 0] -> 0).
        if not pos and len(neg) <= 1:
            return 0
            
        res = 1
        for x in pos:
            res *= x
            
        # If odd number of negatives, drop the one with smallest absolute value
        # (closest to 0) to make the product positive.
        neg.sort()
        if len(neg) % 2 == 1:
            neg.pop()
            
        for x in neg:
            res *= x
            
        return res
