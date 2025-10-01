class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        reserved = defaultdict(set)
        for r, c in reservedSeats:
            reserved[r].add(c)

        res = 2 * n  # initially assume 2 families per row
        for row, cols in reserved.items():
            can_place = 0
            # Check left block (2-5)
            if not (2 in cols or 3 in cols or 4 in cols or 5 in cols):
                can_place += 1
            # Check right block (6-9)
            if not (6 in cols or 7 in cols or 8 in cols or 9 in cols):
                can_place += 1
            # Check middle block (4-7) if neither left nor right works
            if can_place == 0 and not (4 in cols or 5 in cols or 6 in cols or 7 in cols):
                can_place = 1
            res -= 2 - can_place  # reduce families lost in this row

        return res
