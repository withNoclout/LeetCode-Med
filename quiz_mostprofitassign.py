class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        ans = 0
        best = 0
        i = 0
        n = len(jobs)

        for w in worker:
            while i < n and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

