# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0  :
            return head 
        
        length =  1 
        last_node =  head 
        while last_node.next : 
            last_node = last_node.next 
            length += 1

        last_node.next = head 

        k = k % length
        steps_to_new_head = length - k 

        new_tail = head 
        for _ in range( steps_to_new_head - 1 ) :
            new_tail = new_tail.next 

        new_head = new_tail.next 
        new_tail.next = None 
        return new_head 
