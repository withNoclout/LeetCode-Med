class MyCalendarTwo(object):

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        # check if new booking overlaps with existing double-booked intervals
        for s, e in self.overlaps:
            if not (endTime <= s or startTime >= e):
                return False

        # update overlaps list with intersections of new interval and existing bookings
        for s, e in self.booked:
            if not (endTime <= s or startTime >= e):
                self.overlaps.append((max(s, startTime), min(e, endTime)))

        self.booked.append((startTime, endTime))
        return True
