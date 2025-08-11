class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for x in nums:
            if cand1 == x:
                cnt1 += 1
            elif cand2 == x:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = x, 1
            elif cnt2 == 0:
                cand2, cnt2 = x, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        res = []
        n = len(nums)
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > n // 3 and c not in res:
                res.append(c)
        return res
