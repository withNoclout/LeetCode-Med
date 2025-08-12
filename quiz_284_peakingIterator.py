class PeekingIterator(object):
    def __init__(self, iterator):
        self.i = iterator
        self.buf = [self.i.next()] if self.i.hasNext() else []

    def peek(self):
        return self.buf[0]

    def next(self):
        v = self.buf.pop(0)
        if self.i.hasNext():
            self.buf.append(self.i.next())
        return v

    def hasNext(self):
        return len(self.buf) > 0
