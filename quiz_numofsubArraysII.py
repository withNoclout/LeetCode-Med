class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= target:
            count += 1

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1

        return count
