class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        digits = s[1:-1]

        def gen(t):
            res = []
            if len(t) == 1:
                return [t]
            if t[0] == '0' and t[-1] == '0':
                return res  # no valid form
            if t[0] == '0':
                # only "0.xxx" allowed (no trailing zero in fractional)
                if t[-1] != '0':
                    res.append("0." + t[1:])
                return res
            if t[-1] == '0':
                # only integer allowed
                res.append(t)
                return res
            # both integer and decimals
            res.append(t)
            for i in range(1, len(t)):
                res.append(t[:i] + "." + t[i:])
            return res

        ans = []
        n = len(digits)
        for i in range(1, n):
            lefts = gen(digits[:i])
            rights = gen(digits[i:])
            for a in lefts:
                for b in rights:
                    ans.append("({}, {})".format(a, b))
        return ans
