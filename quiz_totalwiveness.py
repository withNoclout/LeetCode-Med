class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
        def count_waviness_upto(n):
            s = str(n)
            length = len(s)
            memo = {}

            # Returns a tuple: (count of valid numbers formed, sum of waviness)
            def dp(idx, prev, pprev, is_less, is_started):
                state = (idx, prev, pprev, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                if idx == length:
                    return 1, 0
                
                limit = int(s[idx]) if not is_less else 9
                total_count = 0
                total_waviness = 0
                
                for digit in range(limit + 1):
                    new_less = is_less or (digit < limit)
                    
                    if not is_started:
                        if digit == 0:
                            # Still processing leading zeros
                            cnt, wav = dp(idx + 1, 10, 10, new_less, False)
                            total_count += cnt
                            total_waviness += wav
                        else:
                            # First non-zero digit placed
                            cnt, wav = dp(idx + 1, digit, 10, new_less, True)
                            total_count += cnt
                            total_waviness += wav
                    else:
                        # Determine if the PREVIOUS digit (prev) is a peak or valley
                        # We need the digit before that (pprev) to exist (i.e., not be the dummy value 10)
                        is_peak_or_valley = False
                        
                        if pprev != 10:
                            is_peak = (prev > pprev) and (prev > digit)
                            is_valley = (prev < pprev) and (prev < digit)
                            if is_peak or is_valley:
                                is_peak_or_valley = True
                        
                        # Recurse for the rest of the number
                        cnt, wav = dp(idx + 1, digit, prev, new_less, True)
                        
                        total_count += cnt
                        # Add waviness from the suffix
                        total_waviness += wav 
                        # Add contribution of the current peak/valley for all valid suffixes
                        if is_peak_or_valley:
                            total_waviness += cnt
                            
                memo[state] = (total_count, total_waviness)
                return total_count, total_waviness

            # Initial call: prev and pprev set to 10 (dummy value > 9)
            return dp(0, 10, 10, False, False)[1]

        return count_waviness_upto(num2) - count_waviness_upto(num1 - 1)
