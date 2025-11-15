class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        limit = 10 ** half
        res = []

        for q in queries:
            num = start + q - 1
            if num >= limit:
                res.append(-1)
                continue
            left = str(num)
            if intLength % 2 == 0:
                pal = left + left[::-1]
            else:
                pal = left + left[-2::-1]
            res.append(int(pal))

        return res
