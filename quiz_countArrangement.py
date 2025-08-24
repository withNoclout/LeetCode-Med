class Solution(object):
    def countArrangement(self, n):
        from functools import lru_cache

        @lru_cache(None)
        def backtrack(pos, used):
            if pos > n:
                return 1
            total = 0
            for num in range(1, n + 1):
                if not (used >> num) & 1:
                    if num % pos == 0 or pos % num == 0:
                        total += backtrack(pos + 1, used | (1 << num))
            return total

        return backtrack(1, 0)


class Solution(object):
    def countArrangement(self, n):
        memo = {}

        def backtrack(pos, used):
            if pos > n:
                return 1
            if (pos, used) in memo:
                return memo[(pos, used)]

            total = 0
            for num in range(1, n + 1):
                if not (used >> num) & 1:
                    if num % pos == 0 or pos % num == 0:
                        total += backtrack(pos + 1, used | (1 << num))

            memo[(pos, used)] = total
            return total

        return backtrack(1, 0)


