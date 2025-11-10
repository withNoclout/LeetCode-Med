# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Helper to reverse a linked list segment
        def reverse_segment(start, k):
            prev = None
            cur = start
            while k > 0 and cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, start, cur  # new_head, new_tail, next_start

        dummy = ListNode(0, head)
        prev = dummy
        group_size = 1
        cur = head

        while cur:
            # find group length
            temp = cur
            cnt = 0
            while temp and cnt < group_size:
                temp = temp.next
                cnt += 1

            if cnt % 2 == 0:
                # reverse the group
                new_head, new_tail, next_start = reverse_segment(cur, cnt)
                prev.next = new_head
                new_tail.next = next_start
                prev = new_tail
                cur = next_start
            else:
                # skip the group
                for _ in range(cnt):
                    prev = cur
                    cur = cur.next

            group_size += 1

        return dummy.next

