from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is None, we remove the head
        if not fast:
            return head.next
        
        # Move both fast and slow until fast reaches the end
        while fast.next:
            fast = fast.nexta
            slow = slow.next
        
        # Skip the target node
        slow.next = slow.next.next
        
        return head
