class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        ca, cb = [0] * 26, [0] * 26
        for ch in a:
            ca[ord(ch) - 97] += 1
        for ch in b:
            cb[ord(ch) - 97] += 1

        res = float('inf')
        for i in range(26):
            res = min(res, len(a) + len(b) - ca[i] - cb[i])

        pa, pb = [0] * 26, [0] * 26
        pa[0], pb[0] = ca[0], cb[0]
        for i in range(1, 26):
            pa[i] = pa[i - 1] + ca[i]
            pb[i] = pb[i - 1] + cb[i]

        for i in range(25):
            res = min(res, len(a) - pa[i] + pb[i])
            res = min(res, len(b) - pb[i] + pa[i])

        return res
