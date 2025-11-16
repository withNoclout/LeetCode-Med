class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(pressedKeys)
        
        dp = [0] * (n + 1)
        dp[0] = 1  # empty prefix
        
        for i in range(1, n + 1):
            c = pressedKeys[i - 1]
            max_run = 4 if c in '79' else 3

            # Look back up to max_run same digits
            for l in range(1, max_run + 1):
                if i - l < 0:
                    break
                if pressedKeys[i - l] != c:
                    break
                dp[i] = (dp[i] + dp[i - l]) % MOD

        return dp[n]
