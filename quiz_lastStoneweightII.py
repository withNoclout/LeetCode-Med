class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        dp = set([0])
        for stone in stones:
            next_dp = set()
            for s in dp:
                next_dp.add(s + stone)
                next_dp.add(s)
            dp = next_dp
        return min(abs(total - 2 * s) for s in dp)
