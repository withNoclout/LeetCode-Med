# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        from collections import defaultdict

        seen = defaultdict(int)   # map serialization -> count
        res = []

        def serialize(node):
            if not node:
                return "#"
            serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            seen[serial] += 1
            if seen[serial] == 2:   # add only once
                res.append(node)
            return serial

        serialize(root)
        return res
