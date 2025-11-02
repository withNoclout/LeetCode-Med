class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(i, prev):
            if i == len(s):
                return True
            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if num == prev - 1 and dfs(j + 1, num):
                    return True
            return False

        for i in range(1, len(s)):
            first = int(s[:i])
            if dfs(i, first):
                return True
        return False
