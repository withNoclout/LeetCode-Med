class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        MAX_AGE = 120
        cnt = [0] * (MAX_AGE + 1)
        for a in ages:
            cnt[a] += 1

        pre = [0] * (MAX_AGE + 1)
        for i in range(1, MAX_AGE + 1):
            pre[i] = pre[i - 1] + cnt[i]

        ans = 0
        for a in range(15, MAX_AGE + 1):  # ages < 15 can never send requests
            if cnt[a] == 0:
                continue
            lower = int(a * 0.5) + 7  # strictly greater than this
            # recipients with age in (lower, a], excluding self
            eligible = pre[a] - pre[lower] - 1
            if eligible > 0:
                ans += cnt[a] * eligible
        return ans
