from itertools import combinations

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.combos = ["".join(c) for c in combinations(characters, combinationLength)]
        self.index = 0

    def next(self):
        """
        :rtype: str
        """
        ans = self.combos[self.index]
        self.index += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combos)
