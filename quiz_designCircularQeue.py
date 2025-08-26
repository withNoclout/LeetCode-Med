class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.capacity
        self.q[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.q[tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.capacity
