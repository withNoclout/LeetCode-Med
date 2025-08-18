"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        dummy = Node(0, None, head, None)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        # detach dummy
        dummy.next.prev = None
        return dummy.next
