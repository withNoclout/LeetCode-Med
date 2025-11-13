class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0

        s = str(abs(num))
        digits = sorted(s)

        if num > 0:
            # place the smallest non-zero first, then all zeros, then remaining digits
            i = 0
            while i < len(digits) and digits[i] == '0':
                i += 1
            first = digits[i]
            zeros = digits[:i]
            rest = digits[i + 1:]
            res_str = first + ''.join(zeros + rest)
            return int(res_str)
        else:
            # for negative numbers, maximize the value then negate
            digits.sort(reverse=True)
            return -int(''.join(digits))
