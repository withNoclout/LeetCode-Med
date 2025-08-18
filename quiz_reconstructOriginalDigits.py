class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        count = Counter(s)
        out = {}

        # unique letters for certain digits
        out[0] = count['z']  # zero
        out[2] = count['w']  # two
        out[4] = count['u']  # four
        out[6] = count['x']  # six
        out[8] = count['g']  # eight

        # now adjust for overlapping
        out[3] = count['h'] - out[8]  # three
        out[5] = count['f'] - out[4]  # five
        out[7] = count['s'] - out[6]  # seven
        out[1] = count['o'] - out[0] - out[2] - out[4]  # one
        out[9] = count['i'] - out[5] - out[6] - out[8]  # nine

        # build result
        res = []
        for i in range(10):
            res.append(str(i) * out.get(i, 0))
        return "".join(res)

