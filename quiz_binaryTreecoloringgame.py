# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: Optional[TreeNode]
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_size = 0
        self.right_size = 0

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                self.left_size = l
                self.right_size = r
            return l + r + 1

        total = dfs(root)
        parent_side = n - (self.left_size + self.right_size + 1)
        # second player wins if can control a region larger than half
        return max(self.left_size, self.right_size, parent_side) > n // 2
