# ...existing code...
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        # If running locally (not on LeetCode), uncomment/define TreeNode:
        # class TreeNode(object):
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right

        if n % 2 == 0:
            return []

        memo = {1: [TreeNode(0)]}
        for m in range(3, n + 1, 2):
            res = []
            for left_nodes in range(1, m, 2):
                right_nodes = m - 1 - left_nodes
                for left in memo[left_nodes]:
                    for right in memo[right_nodes]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            memo[m] = res

        return memo.get(n, [])
#
