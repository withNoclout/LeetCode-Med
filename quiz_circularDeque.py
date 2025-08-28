class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.data = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.data[self.front] = value
        if self.size == 0:
            self.rear = self.front
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.data[self.rear] = value
        if self.size == 0:
            self.front = self.rear
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        if self.size == 0:
            self.front, self.rear = 0, -1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.size == 0:
            self.front, self.rear = 0, -1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k
