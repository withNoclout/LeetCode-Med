from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        buckets = defaultdict(list)
        for w in words:
            if not w:
                # if empty strings are allowed, count them; otherwise ignore
                buckets[''].append((w, 0))
            else:
                buckets[w[0]].append((w, 1))

        ans = len(buckets[''])
        for ch in s:
            waiting = buckets[ch]
            buckets[ch] = []
            for w, i in waiting:
                if i == len(w):
                    ans += 1
                else:
                    buckets[w[i]].append((w, i + 1))
        return ans
