# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        S = set(nums ) 
        cur = head
        ans = 0
        while cur:
            if cur.val in S and (cur.next is None or cur.next.val not in S):
                ans += 1
            cur = cur.next
        return ans
