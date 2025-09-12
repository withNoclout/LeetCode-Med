class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        dp = [1] * 10
        for _ in range(n - 1):
            ndp = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    ndp[j] = (ndp[j] + dp[i]) % MOD
            dp = ndp
        return sum(dp) % MOD
