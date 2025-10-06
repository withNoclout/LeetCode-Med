class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        max_left = max(left) if left else 0
        min_right = min(right) if right else n
        return max(max_left, n - min_right)
