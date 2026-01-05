class Solution(object):
    def kthLargestPerfectSubtree(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        sizes = []

        def dfs(node):
            if not node:
                # Returns: (is_perfect, height)
                # Height 0 represents null
                return True, 0

            l_perfect, l_height = dfs(node.left)
            r_perfect, r_height = dfs(node.right)

            if l_perfect and r_perfect and l_height == r_height:
                height = l_height + 1
                size = (1 << height) - 1
                sizes.append(size)
                return True, height
            
            return False, 0

        dfs(root)
        
        if len(sizes) < k:
            return -1
        
        sizes.sort(reverse=True)
        return sizes[k - 1]
