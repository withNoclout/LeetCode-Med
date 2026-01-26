class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        ans = []
        current = ""
        
        for char in s:
            current += char
            # Greedy check: if the current formed segment is unique, finalize it.
            if current not in seen:
                seen.add(current)
                ans.append(current)
                # Reset for the next segment
                current = ""
        
        return an
