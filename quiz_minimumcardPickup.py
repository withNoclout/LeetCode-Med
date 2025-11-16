class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        last_pos = {}
        ans = float('inf')

        for i, c in enumerate(cards):
            if c in last_pos:
                ans = min(ans, i - last_pos[c] + 1)
            last_pos[c] = i

        return ans if ans != float('inf') else -1
