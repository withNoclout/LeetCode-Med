class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        water = capacity
        steps = 0
        for i, need in enumerate(plants):
            if water < need:
                # go back to river and return
                steps += i * 2
                water = capacity
            water -= need
            steps += 1
        return steps
