class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        res = 0
        max_time = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                res += min(max_time, neededTime[i])
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]
        return res
