class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        is_child = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            is_child.add(child)

        # root is a node that's never a child
        for val in nodes:
            if val not in is_child:
                return nodes[val]
        return None
