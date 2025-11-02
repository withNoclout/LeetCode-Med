class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True
        pre = 0
        for i in range(1, n):
            if i - minJump >= 0 and dp[i - minJump]:
                pre += 1
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                pre -= 1
            dp[i] = pre > 0 and s[i] == '0'
        return dp[-1]
