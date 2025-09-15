class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i = 0
        def build(bound=float('inf')):
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root
        return build()
