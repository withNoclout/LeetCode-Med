class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True
