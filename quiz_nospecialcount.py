class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        limit = int(r**0.5)
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
                    
        special_cnt = 0
        for i in range(limit + 1):
            if is_prime[i]:
                square = i * i
                if square >= l and square <= r:
                    special_cnt += 1
                    
        return (r - l + 1) - special_cnt
