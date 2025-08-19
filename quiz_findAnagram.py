from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        len_p = len(p)
        count_p = Counter(p)
        window = Counter()

        for i, ch in enumerate(s):
            window[ch] += 1
            if i >= len_p:
                left_char = s[i - len_p]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            if window == count_p:
                res.append(i - len_p + 1)
        return res
