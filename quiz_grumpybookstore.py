class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        base = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        extra = 0
        max_extra = 0
        for i in range(n):
            if grumpy[i] == 1:
                extra += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]
            max_extra = max(max_extra, extra)
        return base + max_extra
