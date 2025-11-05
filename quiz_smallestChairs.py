import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
        target_arrival = times[targetFriend][0]

        # Sort friends by arrival time
        sorted_times = sorted(enumerate(times), key=lambda x: x[1][0])

        # Min-heaps:
        # available_chairs keeps track of free chairs (smallest available first)
        # occupied keeps track of (leave_time, chair_index) for occupied chairs
        available_chairs = list(range(n))
        occupied = []

        for friend_index, (arrive, leave) in sorted_times:
            # Free up all chairs from friends who have already left
            while occupied and occupied[0][0] <= arrive:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available_chairs, chair)

            # Assign the smallest available chair
            chair = heapq.heappop(available_chairs)
            heapq.heappush(occupied, (leave, chair))

            # If this is the target friend, return the chair number
            if arrive == target_arrival:
                return chair
O
