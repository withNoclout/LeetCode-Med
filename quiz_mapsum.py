class MapSum(object):

    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.map[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total

