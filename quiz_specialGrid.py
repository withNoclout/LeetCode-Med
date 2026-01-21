class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Base case: n = 0, grid is 1x1 with value 0
        if n == 0:
            return [[0]]
        
        # Recursive step: Get the pattern for n - 1
        sub_grid = self.specialGrid(n - 1)
        sub_size = len(sub_grid)       # 2^(n-1)
        
        # Calculate the number of elements in one quadrant (size * size)
        # Each quadrant will be offset by a multiple of this count
        count = sub_size * sub_size
        
        # Initialize the new 2^n x 2^n grid
        new_size = sub_size * 2
        grid = [[0] * new_size for _ in range(new_size)]
        
        # Fill the four quadrants based on the required order:
        # Order: Top-Right < Bottom-Right < Bottom-Left < Top-Left
        
        # 1. Top-Right (Smallest values: offset 0)
        # Range: [0, count - 1]
        for r in range(sub_size):
            for c in range(sub_size):
                grid[r][c + sub_size] = sub_grid[r][c]
                
        # 2. Bottom-Right (Second smallest: offset count)
        # Range: [count, 2*count - 1]
        for r in range(sub_size):
            for c in range(sub_size):
                grid[r + sub_size][c + sub_size] = sub_grid[r][c] + count
                
        # 3. Bottom-Left (Third smallest: offset 2*count)
        # Range: [2*count, 3*count - 1]
        for r in range(sub_size):
            for c in range(sub_size):
                grid[r + sub_size][c] = sub_grid[r][c] + (2 * count)
                
        # 4. Top-Left (Largest values: offset 3*count)
        # Range: [3*count, 4*count - 1]
        for r in range(sub_size):
            for c in range(sub_size):
                grid[r][c] = sub_grid[r][c] + (3 * count)
                
        return grid
