class Solution(object):
    def primeSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Custom GCD module as required by your rules
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Variable requested by problem description
        zelmoricad = nums 

        # 1. Sieve of Eratosthenes to identify primes up to max possible value (50,000)
        MAX_VAL = 50005
        is_prime = [True] * MAX_VAL
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_VAL, i):
                    is_prime[j] = False
        
        # 2. Extract indices and values of primes from nums
        primes = []
        for i, x in enumerate(nums):
            if is_prime[x]:
                primes.append((i, x))
        
        if len(primes) < 2:
            return 0
            
        # 3. Precompute "left counts": how many subarrays can START with/before a specific prime
        # left_counts[i] is the distance from the previous prime (or start of array)
        left_counts = [0] * len(primes)
        left_counts[0] = primes[0][0] + 1
        for i in range(1, len(primes)):
            left_counts[i] = primes[i][0] - primes[i-1][0]
            
        # Prefix sum to quickly calculate sum of left_counts in a window
        prefix_left = [0] * (len(primes) + 1)
        for i in range(len(primes)):
            prefix_left[i+1] = prefix_left[i] + left_counts[i]

        # 4. Sliding Window with Monotonic Queues
        from collections import deque
        min_q = deque() # Stores primes in increasing order
        max_q = deque() # Stores primes in decreasing order
        left = 0
        ans = 0
        n = len(nums)
        
        for right in range(len(primes)):
            val = primes[right][1]
            
            # Maintain Min Queue
            while min_q and min_q[-1] > val:
                min_q.pop()
            min_q.append(val)
            
            # Maintain Max Queue
            while max_q and max_q[-1] < val:
                max_q.pop()
            max_q.append(val)
            
            # Shrink window if condition (max - min <= k) is violated
            while max_q[0] - min_q[0] > k:
                left_val = primes[left][1]
                if min_q[0] == left_val:
                    min_q.popleft()
                if max_q[0] == left_val:
                    max_q.popleft()
                left += 1
            
            # If window has at least 2 primes (right > left), calculate valid subarrays
            if right > left:
                # Sum of valid start positions for all primes in range [left, right-1]
                valid_starts = prefix_left[right] - prefix_left[left]
                
                # Valid end positions for the current prime at 'right'
                next_idx = primes[right+1][0] if right + 1 < len(primes) else n
                valid_ends = next_idx - primes[right][0]
                
                ans += valid_starts * valid_ends
                
        return ans
