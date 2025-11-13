class Solution(object):
    def rearrangeArray(self, nums):
        pos, neg = [], []
        for x in nums:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)

        res = [0] * len(nums)
        i = j = 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                res[idx] = pos[i]
                i += 1
            else:
                res[idx] = neg[j]
                j += 1
        return res
