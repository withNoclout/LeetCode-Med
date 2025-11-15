class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        bestScore = 0
        best = [0] * 12

        def backtrack(i, arrows, score, arr):
            nonlocal bestScore, best
            if i == 12:
                if score > bestScore:
                    bestScore = score
                    best = arr[:]
                return

            need = aliceArrows[i] + 1

            # Option 1: Bob tries to win this section
            if arrows >= need:
                arr[i] = need
                backtrack(i + 1, arrows - need, score + i, arr)
                arr[i] = 0

            # Option 2: Bob skips this section
            backtrack(i + 1, arrows, score, arr)

        backtrack(0, numArrows, 0, [0] * 12)

        # Add leftover arrows to section 0 (or any)
        leftover = numArrows - sum(best)
        best[0] += leftover
        return best
