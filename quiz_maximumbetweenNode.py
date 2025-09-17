class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(node, min_val, max_val):
            if not node:
                return max_val - min_val
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            return max(helper(node.left, min_val, max_val), helper(node.right, min_val, max_val))
        return helper(root, root.val, root.val)
