class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        max_i = res = 0
        for j in range(1, len(values)):
            max_i = max(max_i, values[j-1] + j-1)
            res = max(res, max_i + values[j] - j)
        return res
