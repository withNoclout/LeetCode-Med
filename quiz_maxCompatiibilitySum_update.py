class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        m, k = len(students), len(students[0])
        # precompute compatibility scores
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                s = 0
                for t in range(k):
                    if students[i][t] == mentors[j][t]:
                        s += 1
                score[i][j] = s

        dp = [-1] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            i = bin(mask).count("1")  # next student index
            if i >= m or dp[mask] < 0:
                continue
            for j in range(m):
                if not (mask & (1 << j)):
                    nmask = mask | (1 << j)
                    val = dp[mask] + score[i][j]
                    if val > dp[nmask]:
                        dp[nmask] = val
        return dp[(1 << m) - 1]
