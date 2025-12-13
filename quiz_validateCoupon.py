class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        def isValid(s):
            if s == "":
                return False
            for c in s:
                if not (c.isalnum() or c == '_'):
                    return False
            return True

        def check(s):
            return s in {"electronics", "grocery", "pharmacy", "restaurant"}

        a = []
        n = len(code)

        for i in range(n):
            if isActive[i]:
                if isValid(code[i]) and check(businessLine[i]):
                    a.append([businessLine[i], code[i]])

        a.sort()
        return [v[1] for v in a]
