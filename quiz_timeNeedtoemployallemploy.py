class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        from collections import defaultdict

        # build tree: manager -> list of subordinates
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        def dfs(emp):
            if not tree[emp]:
                return 0
            return max(dfs(sub) for sub in tree[emp]) + informTime[emp]

        return dfs(headID)
