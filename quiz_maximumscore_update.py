import heapq

class Solution(object):
    def maximumScore(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        # Max-heap to keep track of the largest available numbers.
        # Python's heapq is a min-heap, so we store negative values.
        max_heap = []
        score = 0
        
        for i, num in enumerate(nums):
            # Add the current number to the pool of candidates
            heapq.heappush(max_heap, -num)
            
            # If the current character is '1', it represents a slot that allows us 
            # to secure a value. Since '1's can effectively "pick" any available 
            # position to their left (including current), and we process left-to-right,
            # this '1' forces us to finalize the selection of the best available number.
            if s[i] == '1':
                # Pop the largest value seen so far
                largest = -heapq.heappop(max_heap)
                score += largest
                
        return score
