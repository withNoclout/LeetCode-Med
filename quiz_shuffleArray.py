import random 
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums[:]
        self.array = nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        self.array = self.original[:]
        return self.array 


    def shuffle(self):
        """
        :rtype: List[int]
        """
        arr = self.array[:]
        n = len(arr)
        for i in range(n -1 ,  0  , -1 )   :
            j = random.randint(0 , i ) 
            arr[i] , arr[j] = arr[j] , arr[i]   
        return arr 



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
