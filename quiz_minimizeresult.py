class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        left, right = expression.split('+')
        n, m = len(left), len(right)

        best_val = None
        best_expr = None

        for i in range(n):          # '(' before left[i]
            for j in range(1, m + 1):  # ')' after right[j-1]
                # Parts outside parentheses
                a = int(left[:i]) if i > 0 else 1
                b = int(right[j:]) if j < m else 1

                # Part inside parentheses
                in_left = int(left[i:])
                in_right = int(right[:j])
                inner = in_left + in_right

                val = a * inner * b

                if best_val is None or val < best_val:
                    best_val = val
                    best_expr = left[:i] + '(' + left[i:] + '+' + right[:j] + ')' + right[j:]

        return best_expr
