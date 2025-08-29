class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # count odds and evens in [1..n] and [1..m]
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2

        # odd sum comes from (odd, even) or (even, odd)
        return odd_n * even_m + even_n * odd_m
