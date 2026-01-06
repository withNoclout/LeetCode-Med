from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_s = float('-inf')
        ans_level = 0
        level = 1
        q = deque([root])
        
        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if curr_sum > max_s:
                max_s = curr_sum
                ans_level = level
                
            level += 1
            
        return ans_level
