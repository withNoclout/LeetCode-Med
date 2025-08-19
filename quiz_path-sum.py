# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            res = prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1  # backtrack

            return res

        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)
