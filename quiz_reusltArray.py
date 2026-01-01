import heapq

class Solution(object):
    def resultsArray(self, queries, k):
        """
        :type queries: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        max_heap = []
        results = []
        
        for x, y in queries:
            dist = abs(x) + abs(y)
            # Push negative distance to simulate a max-heap with Python's min-heap
            heapq.heappush(max_heap, -dist)
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
            if len(max_heap) == k:
                results.append(-max_heap[0])
            else:
                results.append(-1)
                
        return results
