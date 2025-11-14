class Solution(object):
    def mergeNodes(self, head):
        dummy = ListNode(0)
        cur_new = dummy
        cur = head.next
        s = 0
        while cur:
            if cur.val == 0:
                cur_new.next = ListNode(s)
                cur_new = cur_new.next
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return dummy.next
