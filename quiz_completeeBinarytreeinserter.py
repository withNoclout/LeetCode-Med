from collections import deque

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.deque = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node = self.deque[0]
        new_node = TreeNode(val)
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.deque.popleft()
        self.deque.append(new_node)
        return node.val

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """

        return self.root
