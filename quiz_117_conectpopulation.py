"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root : 
            return None 
        
        curr = root 
        dummy = Node(0)

        while curr : 
            tail = dummy 
            while curr : 
                if curr.left : 
                    tail.next = curr.left 
                    tail = tail.next 

                if curr.right : 
                    tail.next = curr.right 
                    tail = tail.next 

                curr = curr.next 
            curr = dummy.next 
            dummy.next = None 
        return root 
