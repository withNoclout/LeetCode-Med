class Solution(object):
    def minAnagramLength(self, s):
        n = len(s)
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        common_gcd = 0
        for val in count.values():
            if common_gcd == 0:
                common_gcd = val
            else:
                common_gcd = gcd(common_gcd, val)
                
        # The number of concatenated parts must be a divisor of the GCD of character counts.
        # We want the smallest length, so we want the largest number of parts.
        possible_parts = []
        for i in range(1, int(common_gcd**0.5) + 1):
            if common_gcd % i == 0:
                possible_parts.append(i)
                if i * i != common_gcd:
                    possible_parts.append(common_gcd // i)
        
        possible_parts.sort(reverse=True)
        
        for parts in possible_parts:
            length = n // parts
            base = sorted(s[:length])
            valid = True
            for i in range(length, n, length):
                if sorted(s[i:i+length]) != base:
                    valid = False
                    break
            if valid:
                return length
                
        return n
