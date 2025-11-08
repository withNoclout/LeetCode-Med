from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        n = len(changed)
        if n % 2:
            return []

        cnt = Counter(changed)
        original = []

        # Sort by absolute value to handle zeros and negatives correctly
        for x in sorted(cnt.keys(), key=abs):
            if cnt[x] == 0:
                continue
            need = cnt[x]
            if cnt[2 * x] < need:
                return []
            cnt[2 * x] -= need
            original += [x] * need

        return original
