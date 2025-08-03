# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0 : 
            return [] 
        
        def buildTrees( start , end ) :
            if start > end : 
                return [None  ]
            
            trees = [] 
            for i in range( start , end+ 1 ) :
                left = buildTrees( start , i - 1 )
                right = buildTrees( i + 1 , end )

                for l in left : 
                    for r in right : 
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        trees.append(node)

            return trees 
        
        return buildTrees(1, n)
