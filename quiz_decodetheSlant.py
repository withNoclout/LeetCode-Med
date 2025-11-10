class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 0 or not encodedText:
            return ""
        n = len(encodedText)
        cols = n // rows
        res = []

        # Read along diagonals starting at (0, c0) for c0 in [0..cols-1]
        for c0 in range(cols):
            r, c = 0, c0
            while r < rows and c < cols:
                res.append(encodedText[r * cols + c])
                r += 1
                c += 1

        return "".join(res).rstrip()
