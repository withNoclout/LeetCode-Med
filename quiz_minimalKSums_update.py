class Solution(object):
    def minimalKSum(self, nums, k):
        nums = sorted(set(nums))
        res = 0
        cur = 1

        for x in nums:
            if cur < x and k > 0:
                take = min(k, x - cur)
                res += (cur + (cur + take - 1)) * take // 2
                k -= take
            cur = max(cur, x + 1)

        if k > 0:
            res += (cur + (cur + k - 1)) * k // 2

        return res
