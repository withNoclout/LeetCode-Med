from collections import Counter

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        total = Counter(text)
        n = len(text)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            length1 = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            length2 = k - j - 1 if j < n else 0
            # case: merge two blocks separated by one different char
            merged = length1 + length2
            if merged < total[text[i]]:
                merged += 1
            ans = max(ans, merged)
            # case: single block, maybe extend by one if extra char available
            block = length1
            if block < total[text[i]]:
                block += 1
            ans = max(ans, block)
            i = j
        return ans
