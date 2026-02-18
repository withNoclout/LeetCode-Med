from collections import deque

class RideSharingSystem(object):

    def __init__(self):
        # Queue to store available drivers (FIFO)
        self.drivers = deque()
        
        # Queue to store waiting riders (FIFO)
        self.riders = deque()
        
        # Set to track riders who are currently in the queue (waiting)
        # This helps us validate cancellations.
        self.active_riders = set()
        
        # Set to track riders who have requested cancellation
        # We use "lazy removal" - we only remove them when they reach the front of the queue.
        self.cancelled_riders = set()

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.riders.append(riderId)
        self.active_riders.add(riderId)

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """
        self.drivers.append(driverId)

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        # We need both an available driver and a valid rider
        if not self.drivers:
            return [-1, -1]
        
        # Find the earliest valid rider
        while self.riders:
            rider_id = self.riders.popleft()
            
            # If this rider was cancelled, skip them and check the next one
            if rider_id in self.cancelled_riders:
                # Clean up sets
                self.cancelled_riders.remove(rider_id)
                if rider_id in self.active_riders:
                    self.active_riders.remove(rider_id)
                continue
            
            # If we found a valid rider who is active
            if rider_id in self.active_riders:
                driver_id = self.drivers.popleft()
                
                # Rider is now matched, remove from active set
                self.active_riders.remove(rider_id)
                return [driver_id, rider_id]
        
        # If we exhausted the riders queue and found no one valid
        return [-1, -1]

    def cancelRider(self, riderId):
