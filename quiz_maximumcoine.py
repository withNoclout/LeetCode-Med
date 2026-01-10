class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        coins.sort()
        
        def solve(C):
            res = cur = j = 0
            for i in range(len(C)):
                # Try window starting at C[i][0]
                target = C[i][0] + k - 1
                
                # Expand window to include intervals that start before or at 'target'
                while j < len(C) and C[j][0] <= target:
                    cur += (C[j][1] - C[j][0] + 1) * C[j][2]
                    j += 1
                
                # Subtract overshoot from the last added interval if it goes beyond 'target'
                if j > 0:
                    over = max(0, C[j-1][1] - target)
                    res = max(res, cur - over * C[j-1][2])
                
                # Remove the current interval i from sum as we slide forward
                cur -= (C[i][1] - C[i][0] + 1) * C[i][2]
            return res

        # Check max coins by aligning window start with interval starts
        ans = solve(coins)
        
        # Check max coins by aligning window end with interval ends (using reflection)
        # Map [l, r, w] -> [-r, -l, w]
        ans = max(ans, solve(sorted([[-c[1], -c[0], c[2]] for c in coins])))
        
        return ans
