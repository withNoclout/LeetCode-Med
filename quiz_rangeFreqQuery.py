import bisect

class RangeFreqQuery(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.pos = {}
        for i, v in enumerate(arr):
            if v not in self.pos:
                self.pos[v] = []
            self.pos[v].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        if value not in self.pos:
            return 0
        arr = self.pos[value]
        l = bisect.bisect_left(arr, left)
        r = bisect.bisect_right(arr, right)
        return r - l
