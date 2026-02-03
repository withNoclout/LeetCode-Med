class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        
        # 1. Optimized Sieve to find Smallest Prime Factor (SPF)
        # We only need to sieve up to the maximum number present in nums
        max_val = max(nums)
        spf = list(range(max_val + 1))
        
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                # Optimized slicing for assignment is faster in Python
                spf[i*i : max_val+1 : i] = [i] * len(spf[i*i : max_val+1 : i])

        # 2. Precompute the map: Prime -> List of indices divisible by this prime
        prime_to_indices = {}
        for idx, num in enumerate(nums):
            temp = num
            while temp > 1:
                p = spf[temp]
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(idx)
                while temp % p == 0:
                    temp //= p

        # 3. BFS
        # Queue stores: index
        queue = [0]
        # Distance array, -1 indicates unvisited
        dist = [-1] * n
        dist[0] = 0
        
        visited_primes = set()
        import collections
        q = collections.deque([0])
        
        while q:
            u = q.popleft()
            
            if u == n - 1:
                return dist[u]
            
            d = dist[u]
            
            # Operation 1: Adjacent Step
            for v in (u - 1, u + 1):
                if 0 <= v < n and dist[v] == -1:
                    dist[v] = d + 1
                    q.append(v)
            
            # Operation 2: Prime Teleportation
            # Check if current number is prime
            val = nums[u]
            if val > 1 and spf[val] == val: # val is prime
                p = val
                if p not in visited_primes:
                    visited_primes.add(p)
                    # Visit all indices divisible by p
                    if p in prime_to_indices:
                        for v in prime_to_indices[p]:
                            if dist[v] == -1:
                                dist[v] = d + 1
                                q.append(v)
                                
        return -1
