class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        from collections import Counter
        
        # Count in how many distinct lists (days) each response appears
        counts = Counter()
        for daily_resp in responses:
            # Use set() to deduplicate responses within the same day
            for r in set(daily_resp):
                counts[r] += 1
        
        # Find the response with the highest frequency.
        # Break ties by choosing the lexicographically smallest string.
        best_resp = ""
        max_freq = -1
        
        for resp, freq in counts.items():
            if freq > max_freq:
                max_freq = freq
                best_resp = resp
            elif freq == max_freq:
                if best_resp == "" or resp < best_resp:
                    best_resp = resp
                    
        return best_resp
