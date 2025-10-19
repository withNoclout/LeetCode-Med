class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        # Optimal play: pick stones in descending order of (alice+bob) value.
        stones = sorted(zip(aliceValues, bobValues), key=lambda x: x[0] + x[1], reverse=True)

        alice = bob = 0
        for i, (a, b) in enumerate(stones):
            if i % 2 == 0:   # Alice's turn
                alice += a
            else:            # Bob's turn
                bob += b

        if alice > bob:
            return 1
        if alice < bob:
            return -1
        return 0
