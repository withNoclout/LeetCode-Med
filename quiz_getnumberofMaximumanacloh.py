class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        import heapq
        MOD = 10**9 + 7
        buy = []   # max-heap (use negative price)
        sell = []  # min-heap

        for price, amount, orderType in orders:
            if orderType == 0:  # buy
                while sell and amount > 0 and sell[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell)
                    if sell_amount > amount:
                        heapq.heappush(sell, (sell_price, sell_amount - amount))
                        amount = 0
                    else:
                        amount -= sell_amount
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:  # sell
                while buy and amount > 0 and -buy[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy)
                    if buy_amount > amount:
                        heapq.heappush(buy, (buy_price, buy_amount - amount))
                        amount = 0
                    else:
                        amount -= buy_amount
                if amount > 0:
                    heapq.heappush(sell, (price, amount))

        total = sum(a for _, a in buy + sell) % MOD
        return total
