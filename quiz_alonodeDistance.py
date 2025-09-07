# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root : 
            return [] 
        
        parent = {}
        stack = [root ] 
        while stack :
            node = stack.pop()
            if node.left : 
                parent[node.left] = node 
                stack.append( node.left ) 
            if node.right : 
                parent[node.right ] = node 
                stack.append( node.right ) 

        q = deque([target , 0 ]) 
        seen = {target } 
        res = [] 
        while q : 
            node , d = q.popleft()
            if d  == k : 
                res.append( node.val ) 
                while q and q[0][1] == k : 
                    res.append( q.popleft()[0].val )
                return res 
        for nei in ( node.left , node.right , parent.get(node ) ) :
            if nei and nei not in seen  :
                seen.add(nei) 
                q.append((nei , d + 1 )) 
        return []
