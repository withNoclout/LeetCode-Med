class Solution:
    def fractionToDecimal(self, numerator, denominator) :
        if numerator == 0:
            return "0"

        res = []

        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        res.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(res)

        res.append('.')
        remainder_map = {}

        while remainder:
            if remainder in remainder_map:
                res.insert(remainder_map[remainder], '(')
                res.append(')')
                break

            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(res)
