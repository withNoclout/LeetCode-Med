class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        count_secret = [0] * 10
        count_guess = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                count_secret[int(s)] += 1
                count_guess[int(g)] += 1
        
        cows = sum(min(count_secret[i], count_guess[i]) for i in range(10))
        
        return str(bulls) + "A" + str(cows) + "B"
