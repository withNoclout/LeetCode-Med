class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.count = 0
        # map product_id -> price
        self.price_map = {p: pr for p, pr in zip(products, prices)}

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.count += 1
        total = 0
        for p, a in zip(product, amount):
            total += self.price_map[p] * a

        if self.count % self.n == 0:
            total = total * (100 - self.discount) / 100.0

        return total
