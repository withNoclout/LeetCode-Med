class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        groups = defaultdict(list)
        res = []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        return res
