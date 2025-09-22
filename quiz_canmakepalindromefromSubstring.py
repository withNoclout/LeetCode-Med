class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        prefix = [0] * (n + 1)

        for i in range(n):
            bit = 1 << (ord(s[i]) - ord('a'))
            prefix[i + 1] = prefix[i] ^ bit

        res = []
        for l, r, k in queries:
            mask = prefix[r + 1] ^ prefix[l]
            # count set bits
            odd = bin(mask).count("1")
            res.append(odd // 2 <= k)
        return res
