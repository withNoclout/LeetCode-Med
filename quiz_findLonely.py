from collections import Counter

class Solution(object):
    def findLonely(self, nums):
        cnt = Counter(nums)
        res = []
        for x in nums:
            if cnt[x] == 1 and cnt.get(x - 1, 0) == 0 and cnt.get(x + 1, 0) == 0:
                res.append(x)
        return res
