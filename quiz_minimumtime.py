class Solution(object):
    def minimumTime(self, d, r):
        """
        :type d: List[int]
        :type r: List[int]
        :rtype: int
        """
        d1, d2 = d
        r1, r2 = r
        
        # Helper function to calculate GCD (Greatest Common Divisor)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        # Helper function to calculate LCM (Least Common Multiple)
        def lcm(a, b):
            if a == 0 or b == 0:
                return 0
            return (a * b) // gcd(a, b)
            
        lcm_val = lcm(r1, r2)
        
        def check(time):
            # Calculate how many times each drone recharges in 'time' hours
            c1 = time // r1      # Count of hours D1 is recharging
            c2 = time // r2      # Count of hours D2 is recharging
            cb = time // lcm_val # Count of hours BOTH are recharging
            
            # --- Categorize Available Slots ---
            
            # Slots available ONLY to Drone 1
            # (Occurs when D2 is recharging, but D1 is NOT)
            # This equals: (Total D2 recharge slots) - (Slots where both recharge)
            avail_only_d1 = c2 - cb
            
            # Slots available ONLY to Drone 2
            # (Occurs when D1 is recharging, but D2 is NOT)
            avail_only_d2 = c1 - cb
            
            # Slots available to BOTH (Shared pool)
            # (Occurs when NEITHER is recharging)
            # Total Time - (D1 is recharging OR D2 is recharging)
            # Principle of Inclusion-Exclusion: Union(A, B) = |A| + |B| - |Intersection|
            # Recharging Union = c1 + c2 - cb
            avail_shared = time - (c1 + c2 - cb)
            
            # --- Greedy Allocation ---
            
            # Drone 1 uses its exclusive slots first
            needed_d1 = max(0, d1 - avail_only_d1)
            
            # Drone 2 uses its exclusive slots first
            needed_d2 = max(0, d2 - avail_only_d2)
            
            # Check if the shared slots can cover the remaining needs of both
            return avail_shared >= (needed_d1 + needed_d2)

        # Binary Search for the minimum time
        # Lower bound: at least the total deliveries (best case: no recharging constraints)
        low = d1 + d2
        # Upper bound: A safe estimate. Since r >= 2, we lose at most half the slots.
        # So roughly 2 * total deliveries should be enough. Adding buffer for safety.
        high = (d1 + d2) * max(r1, r2) * 2 + 1000
        
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
