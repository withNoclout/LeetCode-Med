class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, t))

        res = set()
        n = len(parsed)
        for i in range(n):
            name, time, amount, city, raw = parsed[i]
            if amount > 1000:
                res.add(raw)
            for j in range(n):
                if i == j:
                    continue
                n2, t2, a2, c2, raw2 = parsed[j]
                if name == n2 and city != c2 and abs(time - t2) <= 60:
                    res.add(raw)
                    res.add(raw2)
        return list(res)
