# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        # 1) get length
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        base, extra = divmod(n, k)  # first 'extra' parts get one extra node
        res = []
        cur = head

        for i in range(k):
            part_head = cur
            size = base + (1 if i < extra else 0)
            # advance size-1 nodes, then cut
            for _ in range(size - 1):
                if cur:
                    cur = cur.next
            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt
            res.append(part_head)

        return res
