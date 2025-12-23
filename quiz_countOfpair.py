class Solution(object):
    def countOfPairs(self, n, x, y):
        res = [0] * n
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                d = min(abs(i - j), abs(i - x) + 1 + abs(y - j), abs(i - y) + 1 + abs(x - j))
                res[d - 1] += 2
        return res
