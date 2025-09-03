class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tx , ty = target 
        player = abs(tx) +  abs(ty)
        for gx, gy in ghosts:
            if abs(gx - tx) + abs(gy - ty) <= player:
                return False
        return True
