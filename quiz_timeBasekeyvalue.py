import collections
import bisect

class TimeMap(object):

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.store[key]
        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        if i == 0:
            return ""
        return arr[i-1][1]
