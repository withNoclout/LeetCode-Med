class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        res = 1
        for x in arr[1:]:
            if x >= res + 1:
                res += 1
        return res
