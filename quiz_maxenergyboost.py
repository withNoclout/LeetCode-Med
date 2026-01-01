class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        n = len(energyDrinkA)
        dpA = [0] * n
        dpB = [0] * n
        
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        
        if n > 1:
            dpA[1] = dpA[0] + energyDrinkA[1]
            dpB[1] = dpB[0] + energyDrinkB[1]
            
        for i in range(2, n):
            dpA[i] = energyDrinkA[i] + max(dpA[i-1], dpB[i-2])
            dpB[i] = energyDrinkB[i] + max(dpB[i-1], dpA[i-2])
            
        return max(dpA[n-1], dpB[n-1])
