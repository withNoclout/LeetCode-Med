from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = Counter(arr)
        freq = sorted(count.values())
        unique = len(freq)

        for f in freq:
            if k >= f:
                k -= f
                unique -= 1
            else:
                break
        return unique
