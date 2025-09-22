class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(s):
            smallest = min(s)
            return s.count(smallest)

        wfreq = sorted(f(w) for w in words)
        res = []
        n = len(wfreq)
        import bisect
        for q in queries:
            fq = f(q)
            # find how many in wfreq > fq
            idx = bisect.bisect_right(wfreq, fq)
            res.append(n - idx)
        return res
