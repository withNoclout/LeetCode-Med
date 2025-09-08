class Solution : 
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1
        return boats
