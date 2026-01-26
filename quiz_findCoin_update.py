class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        coins = []
        for i, numWay in enumerate(numWays):
            if numWay == 1:
                coin = i+1
                coins.append(coin)
                for j in range(len(numWays)-1, coin-1, -1):
                    if numWays[j] < numWays[j-coin]:
                        return []
                    numWays[j] -= numWays[j-coin]
                numWays[i] = 0
            elif numWay > 1:
                return []
        return coins


        
