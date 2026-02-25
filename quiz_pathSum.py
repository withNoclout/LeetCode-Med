# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
                
            # Get the max path sum from the left and right subtrees.
            # If a subtree returns a negative sum, we ignore it by taking max(0, ...).
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            # Calculate the max path sum if it "peaks" at the current node (U-shape)
            current_u_shape_sum = node.val + left_max + right_max
            
            # Update the global maximum if this local U-shape path is the best so far
            self.max_sum = max(self.max_sum, current_u_shape_sum)
            
            # Return the max path sum that can be extended to the parent node
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return self.max_sum
