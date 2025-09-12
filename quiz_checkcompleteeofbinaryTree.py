class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque
        queue = deque([root])
        end = False
        while queue:
            node = queue.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
