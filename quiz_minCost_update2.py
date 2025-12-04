class Solution(object):
    def minCost(self, nums, x):
        n = len(nums)
        min_costs = list(nums)
        res = sum(min_costs)
        
        for k in range(1, n):
            curr_sum = 0
            for i in range(n):
                min_costs[i] = min(min_costs[i], nums[(i + k) % n])
                curr_sum += min_costs[i]
            res = min(res, curr_sum + k * x)
            
        return res
