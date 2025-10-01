# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.res = max(self.res, length)
            if direction == "L":
                dfs(node.left, "R", length + 1)   # go left, next turn right
                dfs(node.right, "L", 1)           # restart from right child
            else:
                dfs(node.right, "L", length + 1)  # go right, next turn left
                dfs(node.left, "R", 1)            # restart from left child

        dfs(root, "L", 0)
        dfs(root, "R", 0)
        return self.res
