class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n  = len(nums) 
        nums.sort()

        left = nums[:(n +1) // 2] [::-1 ] 
        right = nums[(n + 1) // 2:][::-1] 

        nums[::2] = left
        nums[1::2] = right
