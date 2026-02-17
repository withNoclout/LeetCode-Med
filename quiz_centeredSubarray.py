class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        
        # Iterate over every possible starting index of a subarray
        for i in range(n):
            current_sum = 0
            seen = set()
            
            # Iterate over every possible ending index, expanding the subarray
            for j in range(i, n):
                val = nums[j]
                current_sum += val
                seen.add(val)
                
                # Check condition: Sum of elements equals at least one element in the subarray
                if current_sum in seen:
                    count += 1
                    
        return count
