class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_sum = mean * (m + n)
        known_sum = sum(rolls)
        remain = total_sum - known_sum

        if remain < n or remain > 6 * n:
            return []

        base = remain // n
        extra = remain % n

        res = [base] * n
        for i in range(extra):
            res[i] += 1

        return res
