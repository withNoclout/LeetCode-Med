class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        odd = 0
        for i in range(1, len(encoded), 2):
            odd ^= encoded[i]
        perm = [total ^ odd]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
