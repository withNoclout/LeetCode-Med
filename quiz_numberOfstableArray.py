class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[i][j][0] is number of stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] is number of stable arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        # Base cases: arrays consisting only of a single type of digit within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Calculate stable arrays ending in 0
                # Standard recurrence: adding 0 to any stable array of (i-1, j)
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract invalid cases: arrays that already had 'limit' zeros
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD

                # Calculate stable arrays ending in 1
                # Standard recurrence: adding 1 to any stable array of (i, j-1)
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                # Subtract invalid cases: arrays that already had 'limit' ones
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
