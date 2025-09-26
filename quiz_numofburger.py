class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # Let x = number of jumbo burgers, y = number of small burgers
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        # => x = (tomatoSlices - 2*cheeseSlices) / 2
        #    y = cheeseSlices - x
        if (tomatoSlices % 2) != 0:
            return []
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        if x < 0 or y < 0:
            return []
        return [x, y]
