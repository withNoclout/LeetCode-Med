class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # The first jump must be exactly 1 unit
        if len(stones) > 1 and stones[1] != 1:
            return False
            
        # dp map where key is stone position, value is a set of jump lengths used to reach it
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        
        for stone in stones:
            for k in dp[stone]:
                # Next possible jump distances
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in dp:
                        dp[stone + step].add(step)
                        
        # If the last stone has any jump lengths in its set, it's reachable
        return len(dp[stones[-1]]) > 0
