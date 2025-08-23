class Solution:
    def minimumSum(self, A):
        res = float("inf")
        for _ in range(4):  # rotate 4 times to cover all orientations
            n, m = len(A), len(A[0])
            for i in range(1, n):  # horizontal cut
                a1 = self.minimumArea(A[:i])
                # vertical split on bottom part
                for j in range(1, m):
                    part2 = [row[:j] for row in A[i:]]
                    part3 = [row[j:] for row in A[i:]]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    if a1 and a2 and a3:
                        res = min(res, a1 + a2 + a3)

                # further horizontal split on bottom part
                for i2 in range(i + 1, n):
                    part2 = A[i:i2]
                    part3 = A[i2:]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    if a1 and a2 and a3:
                        res = min(res, a1 + a2 + a3)
            A = self.rotate(A)  # rotate 90 degrees
        return res if res < float("inf") else 0

    def minimumArea(self, A):
        if not A or not A[0]:
            return 0
        n, m = len(A), len(A[0])
        left, top, right, bottom = float("inf"), float("inf"), -1, -1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        if right == -1:  # no ones
            return 0
        return (right - left + 1) * (bottom - top + 1)

    def rotate(self, A):
        n, m = len(A), len(A[0])
        return [[A[i][j] for i in range(n - 1, -1, -1)] for j in range(m)]
