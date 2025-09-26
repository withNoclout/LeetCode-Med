from collections import Counter

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        counter = Counter()
        n = len(s)
        for i in range(n - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                counter[sub] += 1
        return max(counter.values() or [0])
