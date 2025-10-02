class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drank = 0
        empty = 0

        while numBottles > 0:
            # Drink all full bottles
            drank += numBottles
            empty += numBottles
            numBottles = 0

            # Exchange empty bottles if possible
            if empty >= numExchange:
                empty -= numExchange
                numBottles = 1
                numExchange += 1  # after each exchange, requirement increases

        return drank
