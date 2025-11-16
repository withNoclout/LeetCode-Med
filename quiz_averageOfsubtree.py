# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return (0, 0)  # sum, count
            s_left, c_left = dfs(node.left)
            s_right, c_right = dfs(node.right)
            total_sum = s_left + s_right + node.val
            total_cnt = c_left + c_right + 1
            if node.val == total_sum // total_cnt:
                self.ans += 1
            return (total_sum, total_cnt)

        dfs(root)
        return self.ans
