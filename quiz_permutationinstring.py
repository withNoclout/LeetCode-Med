from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = Counter(s1)
        window = Counter(s2[:n])

        if need == window:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            window[s2[i - n]] -= 1
            if window[s2[i - n]] == 0:
                del window[s2[i - n]]
            if window == need:
                return True

        return False
