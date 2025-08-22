class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_mod = { 0 : -1 }
        total = 0
        for i , num in enumerate(nums)  :
            total += num
            if k != 0:
                total %= k
            if total in prefix_mod : 
                if i - prefix_mod[total] > 1:
                    return True
            else:
                prefix_mod[total] = i
        return False    
