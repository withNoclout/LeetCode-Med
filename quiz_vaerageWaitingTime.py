class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        cur_end = 0          # when the chef becomes free
        total_wait = 0L      # use long to avoid overflow in Py2-style typing

        for arrive, time in customers:
            if cur_end < arrive:
                cur_end = arrive
            cur_end += time
            total_wait += cur_end - arrive

        return float(total_wait) / len(customers)
