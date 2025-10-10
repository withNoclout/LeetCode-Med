# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        q = deque([root])
        level = 0
        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                v = node.val
                if level % 2 == 0:
                    if v % 2 == 0:
                        return False
                    if prev is not None and v <= prev:
                        return False
                else:
                    if v % 2 == 1:
                        return False
                    if prev is not None and v >= prev:
                        return False
                prev = v
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
