from collections import deque

class FrontMiddleBackQueue(object):

    def __init__(self):
        self.left = deque()   # first half (could be 1 longer than right)
        self.right = deque()  # second half

    def _rebalance(self):
        # Keep: len(left) == len(right) or len(left) == len(right) + 1
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Insert at index n//2: always ends up at the tail of left
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.append(val)
        self._rebalance()

    def popFront(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self._rebalance()
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        # Middle is the last of left (for even, take the left-middle)
        val = self.left.pop()
        self._rebalance()
        return val

    def popBack(self):
        """
        :rtype: int
        """
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self._rebalance()
        return val
