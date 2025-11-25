class Solution(object):
    def closestPrimes(self, left, right):
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, right + 1, i):
                    is_prime[j] = False
                    
        prev = -1
        min_diff = float('inf')
        res = [-1, -1]
        
        for i in range(left, right + 1):
            if is_prime[i]:
                if prev != -1:
                    diff = i - prev
                    if diff < min_diff:
                        min_diff = diff
                        res = [prev, i]
                        if min_diff <= 2:
                            return res
                prev = i
                
        return res
