class Solution(object):
    def minimumRemoval(self, beans):
        beans.sort()
        total = sum(beans)
        n = len(beans)
        keep = 0
        for i, v in enumerate(beans):
            keep = max(keep, v * (n - i))
        return total - keep
