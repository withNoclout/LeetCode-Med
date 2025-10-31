class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {k: v for k, v in knowledge}
        res = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i + 1:j]
                res.append(d.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
