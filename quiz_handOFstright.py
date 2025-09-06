from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False

        cnt = Counter(hand)
        keys = sorted(cnt.keys())

        for x in keys:
            c = cnt[x]
            if c == 0:
                continue
            # need to use c groups starting at x: x, x+1, ..., x+groupSize-1
            for y in range(x, x + groupSize):
                if cnt[y] < c:
                    return False
                cnt[y] -= c
        return True
