class Solution(object):
    def countDistinct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        length = len(s)
        ans = 0
        
        # 1. Count all valid numbers with strictly fewer digits than n.
        # For a length k, each position can be 1-9 (9 choices). Total = 9^k.
        current_power_of_9 = 9
        for _ in range(length - 1):
            ans += current_power_of_9
            current_power_of_9 *= 9
            
        # 2. Count valid numbers with the same length as n, respecting the limit.
        for i, char in enumerate(s):
            digit = int(char)
            remaining_len = length - 1 - i
            
            if digit == 0:
                # If current digit of n is 0, we can't place any valid digit (1-9) 
                # that keeps the number <= n at this position (since 1 > 0).
                # The prefix itself forces us to stop.
                return ans
            
            # We can place any digit from 1 to (digit - 1) at this position.
            # Following positions can be any digit 1-9 (9 choices).
            ans += (digit - 1) * (9 ** remaining_len)
            
            # We continue the loop effectively "placing" the digit 'digit' itself
            # and moving to check the next position.
        
        # If we finish the loop without hitting a 0, it means n itself is valid (no zeros).
        ans += 1
        
        return ans
