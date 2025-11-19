class Solution(object):
    def countHousePlacements(self, n):
        MOD = 10**9 + 7
        
        house = 1
        space = 1
        total = 2
        
        for _ in range(1, n):
            house = space
            space = total
            total = (house + space) % MOD
        
        return (total * total) % MOD
