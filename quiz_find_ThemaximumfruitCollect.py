dp = [[0] * 1000 for _ in range(1000)]

class Solution:
    def __init__(self):
        self.n = 0

    def init(self):
        for i in range(self.n):
            for j in range(self.n - 1 - i):
                dp[i][j] = 0
            for j in range(self.n - 1 - i, self.n):
                dp[i][j] = -1

    def f2(self, i, j, fruits):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = fruits[i][j] + max(
            self.f2(i - 1, j - 1, fruits),
            self.f2(i - 1, j, fruits),
            self.f2(i - 1, j + 1, fruits)
        )
        return dp[i][j]

    def f3(self, i, j, fruits):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = fruits[i][j] + max(
            self.f3(i - 1, j - 1, fruits),
            self.f3(i, j - 1, fruits),
            self.f3(i + 1, j - 1, fruits)
        )
        return dp[i][j]

    def maxCollectedFruits(self, fruits):
        self.n = len(fruits)
        diag = sum(fruits[i][i] for i in range(self.n))
        self.init()
        child3 = self.f3(self.n - 1, self.n - 2, fruits)
        return diag + child3 + self.f2(self.n - 2, self.n - 1, fruits)
