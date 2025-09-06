class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        # leading zeros
        i = 0
        while i < n and seats[i] == 0:
            i += 1
        best = i  # sit at the very start

        # middle gaps
        prev = i
        for j in range(i + 1, n):
            if seats[j] == 1:
                best = max(best, (j - prev) // 2)
                prev = j

        # trailing zeros
        best = max(best, n - 1 - prev)
        return best
