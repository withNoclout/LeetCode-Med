class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        self.ans = None
        def dfs(node, path):
            if not node:
                return
            path = chr(ord('a') + node.val) + path
            if not node.left and not node.right:
                if self.ans is None or path < self.ans:
                    self.ans = path
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return self.ans
