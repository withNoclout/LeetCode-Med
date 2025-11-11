class Solution(object):
    def goodDaysToRobBank(self, security, time):
        n = len(security)
        if time == 0:
            return list(range(n))
        if n < 2 * time + 1:
            return []

        non_inc = [0] * n  # days of non-increasing before i (inclusive span length - 1)
        non_dec = [0] * n  # days of non-decreasing after i

        # build non-increasing prefix counts
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_inc[i] = non_inc[i - 1] + 1

        # build non-decreasing suffix counts
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        ans = []
        for i in range(time, n - time):
            if non_inc[i] >= time and non_dec[i] >= time:
                ans.append(i)
        return ans
