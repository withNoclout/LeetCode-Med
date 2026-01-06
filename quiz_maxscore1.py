class Solution(object):
    def maxScore(self, n, k, stayScore, travelScore):
        """
        :type n: int
        :type k: int
        :type stayScore: List[List[int]]
        :type travelScore: List[List[int]]
        :rtype: int
        """
        # dp[i] stores the max score achievable ending at city i after the current day
        # Initialize with 0 as we can start at any city
        dp = [0] * n
        
        for d in range(k):
            new_dp = [0] * n
            
            # Phase 1: Initialize new_dp with the option of staying at the current city
            # If we end at city i on day d by staying, we came from city i on day d-1
            for i in range(n):
                new_dp[i] = dp[i] + stayScore[d][i]
            
            # Phase 2: Update new_dp with the option of travelling from i to j
            for i in range(n):
                prev_score = dp[i]
                t_row = travelScore[i]
                for j in range(n):
                    if i != j:
                        # Calculate score if we moved from i to j
                        move_score = prev_score + t_row[j]
                        if move_score > new_dp[j]:
                            new_dp[j] = move_score
            
            dp = new_dp
            
        return max(dp)
