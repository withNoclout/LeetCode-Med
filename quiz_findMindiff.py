class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minute = []

        for t in timePoints:
            h, m = map(int, t.split(':'))
            minute.append(h * 60 + m)

        minute.sort()

        min_diff =  1440 
        for i in range(1 , len(minute)):
            min_diff = min(min_diff, minute[i] - minute[i - 1])
        min_diff = min(min_diff, 1440 - minute[-1] + minute[0])
        return min_diff
    
