# ...existing code...
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        from functools import lru_cache

        @lru_cache(None)
        def build(m):
            if m % 2 == 0:
                return []
            if m == 1:
                return [TreeNode(0)]
            res = []
            for left_nodes in range(1, m, 2):
                right_nodes = m - 1 - left_nodes
                for left in build(left_nodes):
                    for right in build(right_nodes):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return build(n)
#
