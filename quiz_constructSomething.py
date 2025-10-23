class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        length = len(res)

        def backtrack(i):
            # skip filled positions
            while i < length and res[i] != 0:
                i += 1
            if i == length:
                return True

            # try placing largest numbers first for lexicographically largest sequence
            for x in range(n, 0, -1):
                if used[x]:
                    continue
                if x == 1:
                    res[i] = 1
                    used[1] = True
                    if backtrack(i + 1):
                        return True
                    res[i] = 0
                    used[1] = False
                else:
                    j = i + x
                    if j < length and res[j] == 0:
                        res[i] = res[j] = x
                        used[x] = True
                        if backtrack(i + 1):
                            return True
                        res[i] = res[j] = 0
                        used[x] = False
            return False

        backtrack(0)
        return res
