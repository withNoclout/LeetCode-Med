# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = {}
        cur = dummy
        while cur:
            prefix += cur.val
            seen[prefix] = cur
            cur = cur.next
        prefix = 0
        cur = dummy
        while cur:
            prefix += cur.val
            cur.next = seen[prefix].next
            cur = cur.next
        return dummy.next
