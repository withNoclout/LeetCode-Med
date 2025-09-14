class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.moves = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return self.moves
