import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # A dummy node to act as the starting point of the result list
        dummy = ListNode(0)
        current = dummy
        heap = []
        
        # Add the head of each linked list to the heap
        # Use a counter (i) to handle cases where multiple nodes have the same value
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        # While there are nodes in the heap
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Attach the smallest node to our result list
            current.next = node
            current = current.next
            
            # If the extracted node has a next node, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
