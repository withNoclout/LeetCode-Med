class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        from math import ceil 
        times = int(ceil(float(int(b)) / len(a)))
        a *= times
        if b in a:
            return times
        a += a[:len(b)]
        if b in a:
            return times + 1
        return -1
