class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start <= end:
                res.append([start, end])
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return res
