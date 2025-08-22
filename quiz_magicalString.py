class Solution(object):
    def magicalString(self, n):
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1  # already have one '1'
        i = 2     # pointer to how many times to append
        num = 1   # next number to append

        while len(s) < n:
            for _ in range(s[i]):
                s.append(num)
                if num == 1 and len(s) <= n:
                    count += 1
            num = 3 - num  # flip between 1 and 2
            i += 1

        return count
