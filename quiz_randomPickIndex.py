class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0 
        res = -1 
        for i , num in enumerate( self.nums)  :
            if num == target : 
                count += 1 
                if random.randint(0, count - 1) == 0:
                    res = i 


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
