class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can_split(max_sum):
            current_sum = 0
            subarrays = 1
            
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
                    
            return True

        # Binary search boundaries
        left = max(nums)  # The largest single element
        right = sum(nums) # The sum of all elements
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if can_split(mid):
                result = mid       # This sum is possible, but try to find a smaller one
                right = mid - 1
            else:
                left = mid + 1     # This sum is too small, need to increase the allowed sum
                
        return result
