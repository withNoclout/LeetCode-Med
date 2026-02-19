from collections import Counter

class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Count the frequency of each number in the array
        # Example: [20, 10, 30, 30] -> {20: 1, 10: 1, 30: 2}
        counts = Counter(nums)
        
        # Step 2: Count how many numbers share the same frequency
        # We take the values from step 1 (1, 1, 2) and count them.
        # Example: {1: 2, 2: 1} -> Frequency 1 is shared by 2 nums, Frequency 2 is unique.
        freq_of_freqs = Counter(counts.values())
        
        # Step 3: Iterate through the original array to find the first match
        for num in nums:
            frequency = counts[num]
            
            # Check if the frequency of this number appears exactly once among all frequencies
            if freq_of_freqs[frequency] == 1:
                return num
                
        return -1
