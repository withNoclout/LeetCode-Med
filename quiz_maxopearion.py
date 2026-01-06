class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i+1]:
                
                for j in range(2, int(nums[i]**0.5) + 1):
                    if nums[i] % j == 0:
                        nums[i] = j
                        ans += 1
                        break
                        
                if nums[i] > nums[i+1]:
                    return -1
                    
        return ans
