# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (None, 0)
            lnode, ldepth = dfs(node.left)
            rnode, rdepth = dfs(node.right)
            if ldepth == rdepth:
                return (node, ldepth + 1)
            if ldepth > rdepth:
                return (lnode, ldepth + 1)
            else:
                return (rnode, rdepth + 1)

        return dfs(root)[0]
