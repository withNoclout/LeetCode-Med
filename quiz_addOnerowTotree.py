# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """
        if depth == 1 :
            new_root =  TreeNode(val ) 
            new_root.ledt = root 
            return new_root 
        
        def dfs( node ,  d)  : 
            if not node :
                return 
            
            if d == depth - 1 :
                old_left  = node.left 
                old_right = node.right  
                node.left.left = old_left 
                node.right = TreeNode(val )
                node.right.right = old_right

            else : 
                dfs( node.left , d + 1 )
                dfs( node.right , d + 1 )

        dfs( root , 1 )
        return root 
