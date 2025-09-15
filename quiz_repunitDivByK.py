class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        num = 1
        length = 1
        while num % k != 0:
            num = (num * 10 + 1) % k
            length += 1
            if length > k:
                return -1
        return length
