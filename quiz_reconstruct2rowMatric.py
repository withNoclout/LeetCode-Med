class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n

        for i in range(n):
            if colsum[i] == 2:
                top[i] = bottom[i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                # Decide later where to put it
                pass

        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1

        if upper != 0 or lower != 0:
            return []
        return [top, bottom]
