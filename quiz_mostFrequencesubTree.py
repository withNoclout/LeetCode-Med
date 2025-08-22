# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict as defaultDict

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root : 
            return [] 
        count = defaultDict(int)

        def dfs( node  ):
            if not node : 
                return 0 
            
            s = node.val  + dfs(node.left) + dfs(node.right)
            count[s] += 1 
            return s 

        dfs(root)
        max_freq = max(count.values())
        return [k for k, v in count.items() if v == max_freq]
    
