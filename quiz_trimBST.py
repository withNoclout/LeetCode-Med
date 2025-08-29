# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if root.val < low:
            # Entire left subtree is too small
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            # Entire right subtree is too large
            return self.trimBST(root.left, low, high)
        else:
            # Trim both sides
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
