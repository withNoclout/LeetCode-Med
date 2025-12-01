class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        curr_sum = sum(batteries)
        while batteries[-1] > curr_sum // n:
            n -= 1
            curr_sum -= batteries.pop()
        return curr_sum // n
