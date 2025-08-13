class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes ) 
        ugly = [1]* n 
        idx = [0] * m 
        vals = primes[:] 

        for i in range(1, n ) :
            nxt = min(vals ) 
            ugly[i] = nxt  
            for j in range(m) :
                if vals[j] == nxt : 
                    idx[j] += 1
                    vals[j] = ugly[idx[j]] * primes[j]
        return ugly[-1]
