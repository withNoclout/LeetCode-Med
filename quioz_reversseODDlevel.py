class Solution(object):
    def reverseOddLevels(self, root):
        q = [root]
        level = 0
        while q:
            if level % 2:
                for i in range(len(q) // 2):
                    q[i].val, q[~i].val = q[~i].val, q[i].val
            q = [child for node in q for child in (node.left, node.right) if child]
            level += 1
        return root
