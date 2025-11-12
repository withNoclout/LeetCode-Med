from collections import defaultdict

class Solution(object):
    def getDistances(self, arr):
        n = len(arr)
        groups = defaultdict(list)
        for i, v in enumerate(arr):
            groups[v].append(i)

        res = [0] * n
        for idxs in groups.values():
            prefix = [0]
            for x in idxs:
                prefix.append(prefix[-1] + x)
            m = len(idxs)
            for i, x in enumerate(idxs):
                left = x * i - prefix[i]
                right = (prefix[m] - prefix[i + 1]) - x * (m - i - 1)
                res[x] = left + right
        return res

