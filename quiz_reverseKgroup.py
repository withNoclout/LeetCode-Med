class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 1. Check if there are at least k nodes left to reverse
        curr = head
        for _ in range(k):
            if not curr:
                return head # Not enough nodes to reverse, keep as is
            curr = curr.next
        
        # 2. Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 3. After reversal, 'head' is now the tail of this segment.
        # Recursively call for the next part and connect it.
        if curr:
            head.next = self.reverseKGroup(curr, k)
            
        # 4. 'prev' is the new head of this reversed segment
        return prev
