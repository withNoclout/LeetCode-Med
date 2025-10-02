class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        perm = list(range(1, m + 1))
        res = []
        
        for q in queries:
            idx = perm.index(q)
            res.append(idx)
            # Move q to the front
            perm.pop(idx)
            perm.insert(0, q)
        
        return res
