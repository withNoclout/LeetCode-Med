# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        vals = list(map(int, data.split()))
        self.index = 0

        def build(lower, upper):
            if self.index == len(vals):
                return None
            val = vals[self.index]
            if val < lower or val > upper:
                return None

            self.index += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float("-inf"), float("inf"))

