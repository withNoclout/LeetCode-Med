class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        res = 0
        n = len(piles)
        left = 0
        right = n - 1
        while left < right:
            right -= 1        # Bob takes the largest
            res += piles[right]
            right -= 1        # You take the second largest
            left += 1         # Alice takes the smallest
        return res
