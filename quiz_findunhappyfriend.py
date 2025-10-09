class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for j, p in enumerate(preferences[i]):
                rank[i][p] = j

        res = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x][:rank[x][y]]:
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    res += 1
                    break
        return res

