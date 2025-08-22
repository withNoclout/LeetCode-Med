class Solution(object):
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4

        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == side
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                if sides[j] == 0:  # pruning
                    break
            return False

        return backtrack(0)
