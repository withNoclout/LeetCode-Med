class Solution(object):
    def subarrayGCD(self, nums, k):
        import math
        res = 0
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr = math.gcd(curr, nums[j])
                if curr == k:
                    res += 1
                elif curr < k:
                    break
        return res
