class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])
