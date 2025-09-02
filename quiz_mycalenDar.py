class MyCalendar(object):

    def __init__(self):
        self.intervals = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for s, e in self.intervals:
            if not (endTime <= s or startTime >= e):  # overlap
                return False
        self.intervals.append((startTime, endTime))
        return True

