"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)

        def build(x0, y0, length):
            # check if all cells are the same
            first_val = grid[x0][y0]
            all_same = True
            for i in range(x0, x0 + length):
                for j in range(y0, y0 + length):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break

            if all_same:
                return Node(val=bool(first_val), isLeaf=True)

            half = length // 2
            return Node(
                val=True,  # arbitrary, not used for internal nodes
                isLeaf=False,
                topLeft=build(x0, y0, half),
                topRight=build(x0, y0 + half, half),
                bottomLeft=build(x0 + half, y0, half),
                bottomRight=build(x0 + half, y0 + half, half)
            )

        return build(0, 0, n)
