# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        first = last = head

        # move 'first' to kth node from start
        for _ in range(k - 1):
            first = first.next
        kth_from_start = first

        # move 'first' to end to find kth from end
        while first.next:
            first = first.next
            last = last.next
        kth_from_end = last

        # swap values
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        return head
