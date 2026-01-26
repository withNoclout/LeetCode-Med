class Solution(object):
    def gcd(self, a, b):
        """
        Helper GCD function as requested.
        """
        while b:
            a, b = b, a % b
        return a

    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Standard solution for "Minimum Swaps to Sort the Array"
        # Uses Cycle Decomposition
        
        n = len(nums)
        # Store (value, original_index) pairs
        arr_pos = [*enumerate(nums)]
        
        # Sort based on values to find target positions
        arr_pos.sort(key=lambda it: it[1])
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in correct position
            if visited[i] or arr_pos[i][0] == i:
                continue
            
            # Find cycle size
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                # Move to the index where the current element *should* be
                j = arr_pos[j][0]
                cycle_size += 1
            
            # If cycle > 0, we need (cycle_size - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swap
