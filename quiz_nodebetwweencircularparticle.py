# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        idx = 0
        prev = None
        cur = head
        crit_indices = []

        while cur and cur.next:
            nxt = cur.next
            if prev is not None:
                # critical if strictly greater than both neighbors or strictly less
                if (cur.val > prev.val and cur.val > nxt.val) or (cur.val < prev.val and cur.val < nxt.val):
                    crit_indices.append(idx)
            prev = cur
            cur = nxt
            idx += 1

        if len(crit_indices) < 2:
            return [-1, -1]

        min_dist = min(crit_indices[i] - crit_indices[i - 1] for i in range(1, len(crit_indices)))
        max_dist = crit_indices[-1] - crit_indices[0]
        return [min_dist, max_dist]
