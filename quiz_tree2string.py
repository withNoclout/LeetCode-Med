class Solution(object):
    def tree2str(self, root):
        if not root:
            return ""

        # leaf node
        if not root.left and not root.right:
            return str(root.val)

        # if left is missing but right exists, we must add "()"
        if not root.left:
            return str(root.val) + "()" + "(" + self.tree2str(root.right) + ")"

        # if both children
        if root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"

        # only left child
        return str(root.val) + "(" + self.tree2str(root.left) + ")"
