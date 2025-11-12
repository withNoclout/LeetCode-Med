class Solution(object):
    def executeInstructions(self, n, startPos, s):
        m = len(s)
        ans = [0] * m
        for i in range(m):
            r, c = startPos
            steps = 0
            for j in range(i, m):
                ch = s[j]
                if ch == 'U':
                    r -= 1
                elif ch == 'D':
                    r += 1
                elif ch == 'L':
                    c -= 1
                else:  # 'R'
                    c += 1
                if 0 <= r < n and 0 <= c < n:
                    steps += 1
                else:
                    break
            ans[i] = steps
        return ans
