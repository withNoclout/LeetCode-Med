# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # Find node before index a (prev_a) and node at index b (node_b)
        prev_a = None
        cur = list1
        idx = 0
        while idx < a:
            prev_a = cur
            cur = cur.next
            idx += 1
        node_b = cur
        while idx < b:
            node_b = node_b.next
            idx += 1

        # Find tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Connect: prev_a -> list2 -> tail2 -> node_b.next
        if prev_a:
            prev_a.next = list2
        else:
            # (Safeguard for a == 0; per constraints a >= 1, but handle anyway)
            list1 = list2
        tail2.next = node_b.next

        return list1
