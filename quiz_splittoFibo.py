class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        n = len(num)
        path = []

        def dfs(i):
            if i == n and len(path) >= 3:
                return True
            val = 0
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                val = val * 10 + ord(num[j]) - 48
                if val > 2**31 - 1:
                    break
                if len(path) >= 2:
                    s = path[-1] + path[-2]
                    if val < s:
                        continue
                    if val > s:
                        break
                path.append(val)
                if dfs(j + 1):
                    return True
                path.pop()
            return False

        return path if dfs(0) else []
