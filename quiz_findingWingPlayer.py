class Solution(object):
    def findWinningPlayer(self, skills, k):
        cur_winner = 0
        cur_wins = 0
        n = len(skills)
        
        for i in range(1, n):
            if skills[i] > skills[cur_winner]:
                cur_winner = i
                cur_wins = 1
            else:
                cur_wins += 1
            
            if cur_wins == k:
                return cur_winner
                
        return cur_winner
