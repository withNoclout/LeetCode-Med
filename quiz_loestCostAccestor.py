# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a ,b  = p.val , q.val 
        node = root 
        while node : 
            if a < node.val and b < node.val : 
                node  = node.left 
            elif a > node.val and b > node.val :
                node = node.right 
            else : 
                return node 
