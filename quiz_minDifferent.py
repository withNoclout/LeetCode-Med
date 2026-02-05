# Precompute divisors for all numbers up to 100,000.
# This runs once when the script is loaded, making individual test cases very fast.
MX = 100001
g = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        g[j].append(i)

class Solution(object):
    def minDifference(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        self.best_diff = float('inf')
        self.ans = []
        path = [0] * k
        
        # DFS function
        # idx: current index in the path we are filling (from 0 to k-1)
        # target: the number we need to decompose for the remaining slots
        # current_min: minimum factor used so far in the path
        # current_max: maximum factor used so far in the path
        # last_factor: the value of the previously chosen factor (to enforce non-decreasing order)
        def dfs(idx, target, current_min, current_max, last_factor):
            # Optimization: If the current difference already exceeds the best found, prune.
            # (Only applicable if we have a valid complete range, but here min/max are partial.
            # However, max-min can only increase, so if current_max - current_min >= self.best_diff, return)
            if idx < k - 1 and current_max != -1:
                if current_max - current_min >= self.best_diff:
                    return

            # Base Case: We are at the last slot (idx == k-1)
            # The remaining 'target' must be the last factor.
            if idx == k - 1:
                # Enforce non-decreasing order to avoid duplicates
                if target < last_factor:
                    return
                
                final_min = min(current_min, target) if current_min != float('inf') else target
                final_max = max(current_max, target) if current_max != -1 else target
                
                diff = final_max - final_min
                
                if diff < self.best_diff:
                    self.best_diff = diff
                    path[idx] = target
                    self.ans = list(path)
                return

            # Recursive Step: Try all divisors of 'target'
            # We iterate through precomputed divisors g[target]
            for factor in g[target]:
                # Enforce non-decreasing order
                if factor < last_factor:
                    continue
                
                # Optimization: If picking 'factor' leaves a remainder that is too small 
                # to be filled by (k - 1 - idx) factors each >= factor, prune.
                # Remaining product needed: target // factor
                # Minimum product achievable: factor ** (k - 1 - idx)
                # If target // factor < factor ** (remaining_slots), we can't fill it sorted.
                remaining_slots = k - 1 - idx
                if (target // factor) < (factor ** remaining_slots):
                     # Since divisors are sorted, larger factors will also fail
                    break
                
                path[idx] = factor
                new_min = min(current_min, factor) if current_min != float('inf') else factor
                new_max = max(current_max, factor) if current_max != -1 else factor
                
                dfs(idx + 1, target // factor, new_min, new_max, factor)

        dfs(0, n, float('inf'), -1, 1)
        return self.ans
