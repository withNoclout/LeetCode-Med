class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        lo, hi = 0.0, 1.0
        while True:
            mid = (lo + hi) / 2.0
            count = 0
            i = 0
            p = q = 0
            best = 0.0

            for j in range(1, n):
                while i < j and arr[i] <= mid * arr[j]:
                    i += 1
                count += i
                if i > 0:
                    frac = arr[i - 1] * 1.0 / arr[j]
                    if frac > best:
                        best = frac
                        p, q = arr[i - 1], arr[j]

            if count == k:
                return [p, q]
            elif count < k:
                lo = mid
            else:
                hi = mid
