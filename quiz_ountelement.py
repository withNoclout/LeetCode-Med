class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # If k is larger than the number of elements, no element can have k greater elements.
        if k >= n:
            return 0
            
        # Sort the array to order elements by magnitude
        nums.sort()
        
        # The element at index (n - k) is the k-th largest candidate.
        # Any qualified element must be strictly smaller than this value.
        # (Because the elements from index n-k to n-1 represent the 'k' largest values).
        threshold = nums[n - k]
        
        # Since nums is sorted, nums.index(threshold) returns the index of the 
        # first occurrence of 'threshold'. This index is exactly equal to the 
        # count of elements strictly smaller than 'threshold'.
        return nums.index(threshold)
