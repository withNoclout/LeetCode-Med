class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(candiesCount)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + candiesCount[i]

        res = []
        for t, day, cap in queries:
            min_eat = day + 1
            max_eat = (day + 1) * cap
            can = not (max_eat <= prefix[t] or min_eat > prefix[t + 1])
            res.append(can)
        return res
