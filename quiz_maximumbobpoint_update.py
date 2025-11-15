class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        self.ans = [0] * 12
        self.maxScore = 0

        def solve(numArrows, indices, idx, score):
            if numArrows <= 0 or idx == 12:
                if score > self.maxScore:
                    self.maxScore = score
                    res = [0] * 12
                    for i in range(12):
                        if indices & (1 << i):
                            res[i] = aliceArrows[i] + 1
                    res[0] += numArrows
                    self.ans = res
                return

            if numArrows > aliceArrows[idx]:
                solve(numArrows - (aliceArrows[idx] + 1),
                      indices | (1 << idx),
                      idx + 1,
                      score + idx)

            solve(numArrows, indices, idx + 1, score)

        solve(numArrows, 0, 0, 0)
        return self.ans
