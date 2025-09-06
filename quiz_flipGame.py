class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        banned = { x for x , y in zip( fronts , backs   ) if x == y } 
        ans = float('inf')

        for x in fronts + backs :
            if x not in banned and x < ans : 
                ans = x 
        return 0 if ans == float('inf' ) else ans 
