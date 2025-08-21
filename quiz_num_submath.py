class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            stack = []
            sum_in_row = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    sum_in_row[j] = sum_in_row[prev_index] + heights[j] * (j - prev_index)
                else:
                    sum_in_row[j] = heights[j] * (j + 1)
                stack.append(j)
                res += sum_in_row[j]

        return res
