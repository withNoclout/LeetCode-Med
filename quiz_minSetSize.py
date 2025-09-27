class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)

        res, removed, half = 0, 0, len(arr) // 2
        for c in counts:
            removed += c
            res += 1
            if removed >= half:
                break
        return res
