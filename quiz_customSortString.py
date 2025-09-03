from collections import Counter

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        res = []
        for ch in order:
            if ch in cnt:
                res.append(ch * cnt[ch])
                del cnt[ch]
        for ch, c in cnt.items():
            res.append(ch * c)
        return "".join(res)
