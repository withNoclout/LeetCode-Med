import heapq

class Solution(object):
    def minOperations(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Sieve of Eratosthenes to find primes up to 10000 (since n, m < 10^4)
        MAX_VAL = 10000
        is_prime = [True] * MAX_VAL
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_VAL, i):
                    is_prime[j] = False
        
        # If start or end number is prime, valid path is impossible
        if is_prime[n] or is_prime[m]:
            return -1
            
        # Dijkstra's Algorithm
        # Priority Queue stores: (total_cost, current_number)
        pq = [(n, n)]
        # dist array to track minimum cost to reach each number
        dist = {n: n}
        
        n_str_len = len(str(n))
        
        while pq:
            curr_cost, curr_val = heapq.heappop(pq)
            
            if curr_val == m:
                return curr_cost
            
            if curr_cost > dist[curr_val]:
                continue
                
            s = str(curr_val)
            
            # Try changing each digit
            for i in range(len(s)):
                original_digit = int(s[i])
                
                # Try increasing digit
                if original_digit < 9:
                    next_val = curr_val + (10 ** (len(s) - 1 - i))
                    if not is_prime[next_val]:
                        new_cost = curr_cost + next_val
                        if new_cost < dist.get(next_val, float('inf')):
                            dist[next_val] = new_cost
                            heapq.heappush(pq, (new_cost, next_val))
                            
                # Try decreasing digit
                if original_digit > 0:
                    # Special check: cannot decrease leading digit to 0 if length > 1
                    # (must maintain same number of digits)
                    if i == 0 and original_digit == 1 and len(s) > 1:
                        pass
                    else:
                        next_val = curr_val - (10 ** (len(s) - 1 - i))
                        if not is_prime[next_val]:
                            new_cost = curr_cost + next_val
                            if new_cost < dist.get(next_val, float('inf')):
                                dist[next_val] = new_cost
                                heapq.heappush(pq, (new_cost, next_val))
                                
        return -1
