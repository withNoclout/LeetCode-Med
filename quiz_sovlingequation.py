class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(expr):
            coef, const = 0, 0   # coef for x, const for numbers
            i, sign = 0, 1
            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j] not in ['+', '-']:
                        j += 1
                    token = expr[i:j]
                    if token.endswith('x'):
                        num = token[:-1]
                        if num == '':
                            coef += sign
                        else:
                            coef += sign * int(num)
                    else:
                        const += sign * int(token)
                    i = j
            return coef, const

        left, right = equation.split('=')
        coefL, constL = parse(left)
        coefR, constR = parse(right)

        coef = coefL - coefR
        const = constR - constL

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(const // coef)
