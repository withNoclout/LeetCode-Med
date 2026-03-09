import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. Create events: (x, negative_height for start, positive_height for end)
        # Using negative height for start events helps with sorting logic.
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r)) # Start event
            events.append((r, h, 0))   # End event
        
        # 2. Sort events by x-coordinate, then by height
        events.sort()
        
        # 3. Max-heap to store active building heights, initialized with ground (0)
        # We store (height, right_edge) to know when to remove a building.
        max_heap = [(0, float('inf'))]
        res = [[0, 0]] # Placeholder to check for height changes

        for x, h, r in events:
            if h < 0: # Start event
                heapq.heappush(max_heap, (h, r))
            
            # 4. Clean up the heap: remove buildings that have already ended
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            
            # 5. If the current max height changed, it's a key point
            curr_max_height = -max_heap[0][0]
            if res[-1][1] != curr_max_height:
                res.append([x, curr_max_height])
        
        return res[1:] # Remove the initial placeholder
