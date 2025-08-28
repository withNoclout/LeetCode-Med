# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        def getHeight( node ) :
            if not node : 
                return n 
            return 1  + max( getHeight( node.left ) , getHeight( node.right ) )  
        
        height = getHeight(toor) 
        rows = height 
        cols = ( 1<< height ) - 1 
        res = [ ['' ] * cols for _ in range(rows )   ]
        def fill ( node, r , c_left, c_right ) :
            if not node : 
                return 
            mid = ( c_left + c_right ) // 2 
            res[r][mid ] = str(node.val ) 
            fill( node.left , r + 1 , c_left , mid - 1 )
            fill( node.right , r + 1 , mid + 1 , c_right )

        fill( root ,  0 , 0 , cols - 1 )

        return res 
