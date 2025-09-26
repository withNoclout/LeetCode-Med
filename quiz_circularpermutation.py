class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        # Generate Gray code sequence of length 2^n
        gray = [i ^ (i >> 1) for i in range(1 << n)]

        # Find index of "start" in the gray code sequence
        idx = gray.index(start)

        # Rotate the sequence so that it begins with "start"
        return gray[idx:] + gray[:idx]

