class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []
            # top
            for j in range(layer, n - layer):
                elems.append(grid[layer][j])
            # right
            for i in range(layer + 1, m - layer - 1):
                elems.append(grid[i][n - layer - 1])
            # bottom
            for j in range(n - layer - 1, layer - 1, -1):
                elems.append(grid[m - layer - 1][j])
            # left
            for i in range(m - layer - 2, layer, -1):
                elems.append(grid[i][layer])

            k_mod = k % len(elems)
            rotated = elems[k_mod:] + elems[:k_mod]

            idx = 0
            # top
            for j in range(layer, n - layer):
                grid[layer][j] = rotated[idx]
                idx += 1
            # right
            for i in range(layer + 1, m - layer - 1):
                grid[i][n - layer - 1] = rotated[idx]
                idx += 1
            # bottom
            for j in range(n - layer - 1, layer - 1, -1):
                grid[m - layer - 1][j] = rotated[idx]
