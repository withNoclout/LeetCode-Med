class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints)
        if k == n:
            return total

        # Sliding window: find minimum sum subarray of length n-k
        window = sum(cardPoints[:n-k])
        min_sum = window
        for i in range(n-k, n):
            window += cardPoints[i] - cardPoints[i-(n-k)]
            min_sum = min(min_sum, window)

        return total - min_sum
