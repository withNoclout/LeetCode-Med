from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        i, n = 0, len(expression)
        result = Fraction(0, 1)

        while i < n:
            # find the sign
            sign = 1
            if expression[i] in "+-":
                if expression[i] == "-":
                    sign = -1
                i += 1

            # parse numerator
            j = i
            while expression[j] != "/":
                j += 1
            numerator = int(expression[i:j]) * sign

            # parse denominator
            i = j + 1
            j = i
            while j < n and expression[j] not in "+-":
                j += 1
            denominator = int(expression[i:j])

            # add fraction
            result += Fraction(numerator, denominator)
            i = j

        return str(result.numerator) + "/" + str(result.denominator)
