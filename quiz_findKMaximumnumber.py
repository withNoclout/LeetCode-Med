class Solution(object):
    def findMaximumNumber(self, k, x):
        def count(n):
            res = 0
            i = x
            # Count set bits at positions x, 2x, 3x... for numbers 1 to n
            while (1 << (i - 1)) <= n:
                period = 1 << i
                half = period >> 1
                
                # Calculate how many full cycles of 0s and 1s fit in (n + 1)
                res += ((n + 1) // period) * half
                
                # Add remaining bits from the partial cycle
                res += max(0, (n + 1) % period - half)
                
                i += x
            return res

        left, right = 1, 10**16
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if count(mid) <= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
