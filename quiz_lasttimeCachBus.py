class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        p = 0
        m = len(passengers)
        last_bus = buses[-1]
        last_boarded = -1

        for b in buses:
            c = capacity
            while p < m and passengers[p] <= b and c > 0:
                last_boarded = passengers[p]
                p += 1
                c -= 1
            # after loop, c is remaining capacity for this bus
            if b == last_bus:
                remaining = c

        taken = set(passengers)
        if remaining > 0:
            t = last_bus
        else:
            t = last_boarded - 1

        while t in taken:
            t -= 1
        return t
