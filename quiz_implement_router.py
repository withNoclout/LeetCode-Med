from collections import deque, defaultdict

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.queue = deque()  # Each packet: (source, destination, timestamp)
        self.dest_map = defaultdict(list)  # destination -> list of timestamps

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        if len(self.queue) >= self.memoryLimit:
            return False
        self.queue.append((source, destination, timestamp))
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        # Remove timestamp from dest_map[destination]
        self.dest_map[destination].remove(timestamp)
        return [source, destination, timestamp]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        # Count timestamps in [startTime, endTime]
        return sum(startTime <= t <= endTime for t in self.dest_map[destination])
