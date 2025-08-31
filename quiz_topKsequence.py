from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = Counter(words)
        return sorted(cnt.keys(), key=lambda w: (-cnt[w], w))[:k]
