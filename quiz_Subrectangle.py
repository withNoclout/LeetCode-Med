class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float("inf")
        prefix = {0: -1}
        curr_sum = 0
        best = [INF] * n
        res = INF
        min_len = INF

        for i, x in enumerate(arr):
            curr_sum += x
            if curr_sum - target in prefix:
                start = prefix[curr_sum - target] + 1
                length = i - start + 1
                if start > 0 and best[start - 1] != INF:
                    res = min(res, best[start - 1] + length)
                min_len = min(min_len, length)
            best[i] = min_len
            prefix[curr_sum] = i

        return res if res != INF else -1
