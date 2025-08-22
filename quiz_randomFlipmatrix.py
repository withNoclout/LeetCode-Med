import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = {}
        self.remaining = self.total

    def flip(self):
        """
        :rtype: List[int]
        """
        r = random.randint(0, self.remaining - 1)
        self.remaining -= 1

        x = self.flipped.get(r, r)
        self.flipped[r] = self.flipped.get(self.remaining, self.remaining)

        return [x // self.n, x % self.n]

    def reset(self):
        """
        :rtype: None
        """
        self.flipped.clear()
        self.remaining = self.total
