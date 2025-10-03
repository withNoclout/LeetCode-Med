class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        sets = [set(fc) for fc in favoriteCompanies]
        res = []
        for i, s in enumerate(sets):
            is_subset = False
            for j, t in enumerate(sets):
                if i != j and s.issubset(t):
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)
        return res
