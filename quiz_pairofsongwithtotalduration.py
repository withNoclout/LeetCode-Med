class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter()
        res = 0
        for t in time:
            res += count[(60 - t % 60) % 60]
            count[t % 60] += 1
        return res
