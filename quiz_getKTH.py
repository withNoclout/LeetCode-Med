class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        memo = {1: 0}

        def power(x):
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                memo[x] = 1 + power(x // 2)
            else:
                memo[x] = 1 + power(3 * x + 1)
            return memo[x]

        arr = list(range(lo, hi + 1))
        arr.sort(key=lambda x: (power(x), x))
        return arr[k - 1]
