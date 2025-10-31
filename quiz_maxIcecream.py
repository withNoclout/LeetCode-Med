class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        for c in costs:
            if coins >= c:
                coins -= c
                count += 1
            else:
                break
        return count
