class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        val_set = set(arr)

        for i, x in enumerate(arr):
            ways = 1  # the single-node tree
            for j in range(i):
                a = arr[j]
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        ways = (ways + dp[a] * dp[b]) % MOD
            dp[x] = ways

        return sum(dp.values()) % MOD
