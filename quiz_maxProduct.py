# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(s)
            return s

        total_sum = dfs(root)
        best = 0
        for s in subtree_sums:
            best = max(best, s * (total_sum - s))
        return best % MOD
