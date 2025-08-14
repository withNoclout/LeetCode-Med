# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node ) :
            if not node :         
                return ( 0,0 ) 
            
            left = dfs(node.left)
            right = dfs(node.right ) 
            rob_this = node.val + left[1] + right [1] 
            skip_this = max(left ) + max( right ) 
            return (rob_this, skip_this)
        


        return max(dfs(root))
