class Solution(object):
    def sumDistance(self, nums, s, d):
        MOD = 10**9 + 7
        for i in range(len(nums)):
            nums[i] += d if s[i] == 'R' else -d
            
        nums.sort()
        res = 0
        prefix = 0
        for i, x in enumerate(nums):
            res = (res + i * x - prefix) % MOD
            prefix += x
        return res
