class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        user_minutes = defaultdict(set)
        for uid, minute in logs:
            user_minutes[uid].add(minute)

        res = [0] * k
        for minutes in user_minutes.values():
            if len(minutes) <= k:
                res[len(minutes) - 1] += 1
        return res
