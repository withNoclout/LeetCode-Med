class Solution(object):
    def minimumPartition(self, s, k):
        res = 1
        curr = 0
        for d in s:
            val = int(d)
            if val > k: return -1
            curr = curr * 10 + val
            if curr > k:
                res += 1
                curr = val
        return res
