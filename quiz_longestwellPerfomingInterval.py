class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        score = 0
        seen = {}
        res = 0
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                res = i + 1
            else:
                if score - 1 in seen:
                    res = max(res, i - seen[score - 1])
            if score not in seen:
                seen[score] = i
        return res
