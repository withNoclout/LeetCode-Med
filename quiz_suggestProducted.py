class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            suggestions = []
            for p in products:
                if p.startswith(prefix):
                    suggestions.append(p)
                if len(suggestions) == 3:
                    break
            res.append(suggestions)
        return res

