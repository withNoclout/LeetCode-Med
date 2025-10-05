class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        return arr[:k]
1
