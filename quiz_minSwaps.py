class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        trailing_zeros = []

        # Count trailing zeros in each row
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and trailing_zeros[j] < need:
                j += 1
            if j == n:
                return -1
            swaps += j - i
            # move row j to i
            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                j -= 1

        return swaps
