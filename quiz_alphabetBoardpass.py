class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        def pos(c):
            idx = ord(c) - ord('a')
            return divmod(idx, 5)  # (row, col)

        res = []
        cur_r, cur_c = 0, 0
        for ch in target:
            r, c = pos(ch)
            # Special care: move UP/LEFT before DOWN/RIGHT to avoid invalid moves at 'z'
            while cur_r > r:
                res.append('U')
                cur_r -= 1
            while cur_c > c:
                res.append('L')
                cur_c -= 1
            while cur_r < r:
                res.append('D')
                cur_r += 1
            while cur_c < c:
                res.append('R')
                cur_c += 1
            res.append('!')
        return ''.join(res)
