# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, path):
            if not node:
                return 0
            path ^= (1 << node.val)   # toggle bit for this value
            if not node.left and not node.right:  # leaf node
                return 1 if path & (path - 1) == 0 else 0
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
