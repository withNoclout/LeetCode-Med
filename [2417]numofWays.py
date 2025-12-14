class Solution(object):
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        if not seats or len(seats) % 2 == 1:
            return 0
            
        res = 1
        for i in range(2, len(seats), 2):
            res = (res * (seats[i] - seats[i-1])) % MOD
            
        return res