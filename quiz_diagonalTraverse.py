class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        diagonals = defaultdict(list)

        # Group elements by i+j (diagonal index)
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diagonals[i + j].append(val)

        res = []
        # Traverse diagonals in order
        for k in sorted(diagonals.keys()):
            # reverse each diagonal because we want bottom-up order
            res.extend(reversed(diagonals[k]))

        return res
