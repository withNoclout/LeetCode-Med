from collections import deque 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root : 
            return [] 
        
        res = [] 
        q = deque([root]) 
        while q :
            level_max = float('-inf')
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            res.append(level_max)
        return res
    
