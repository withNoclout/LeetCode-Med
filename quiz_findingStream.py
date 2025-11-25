class DataStream(object):

    def __init__(self, value, k):
        self.val = value
        self.k = k
        self.cnt = 0

    def consec(self, num):
        if num == self.val:
            self.cnt += 1
        else:
            self.cnt = 0
        return self.cnt >= self.k
