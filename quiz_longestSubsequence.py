import bisect

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_lis_length(arr):
            """
            Standard O(N log N) function to find LIS length using Patience Sorting
            """
            if not arr:
                return 0
            tails = []
            for x in arr:
                # Find the first element in tails that is >= x
                idx = bisect.bisect_left(tails, x)
                
                # If x is greater than all tail elements, extend the longest subsequence
                if idx < len(tails):
                    # Replace the existing element to maintain the smallest tail for this length
                    # This step maintains the "strictly increasing" property naturally:
                    # if x is equal to tails[idx], we replace it with itself (no extension).
                    tails[idx] = x
                else:
                    tails.append(x)
            return len(tails)

        max_len = 0
        
        # Iterate through each bit position (0 to 30 covers typical integer range)
        for bit in range(31):
            # Create a subset of numbers that have the current bit set
            subset = [x for x in nums if (x >> bit) & 1]
            
            # If no numbers have this bit set, skip
            if not subset:
                continue
                
            # Find the LIS of this subset and update the global maximum
            max_len = max(max_len, get_lis_length(subset))
            
        return max_len
