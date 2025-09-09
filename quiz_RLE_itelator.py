# ...existing code...
class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        # store encoding and current index pointing at the count for current value
        self.encoding = encoding
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        # consume n items from the run-length encoding
        while self.i < len(self.encoding) and n > 0:
            cnt = self.encoding[self.i]
            if cnt == 0:
                self.i += 2
                continue
            if cnt >= n:
                # consume n from current run and return its value
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            else:
                # skip this run entirely
                n -= cnt
                self.i += 2
        return -1
#
