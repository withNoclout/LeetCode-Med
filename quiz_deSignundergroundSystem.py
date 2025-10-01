class UndergroundSystem(object):

    def __init__(self):
        # Store active check-ins: id -> (stationName, time)
        self.checkins = {}
        # Store travel times: (startStation, endStation) -> (totalTime, tripCount)
        self.travel_times = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.checkins.pop(id)
        duration = t - startTime
        key = (startStation, stationName)

        if key not in self.travel_times:
            self.travel_times[key] = [0, 0]  # [totalTime, tripCount]

        self.travel_times[key][0] += duration
        self.travel_times[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        totalTime, tripCount = self.travel_times[(startStation, endStation)]
        return float(totalTime) / tripCount
