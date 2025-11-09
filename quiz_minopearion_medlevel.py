class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr = [v for row in grid for v in row]
        # Check feasibility: all values must be congruent mod x
        r = arr[0] % x
        for v in arr:
            if v % x != r:
                return -1

        arr.sort()
        m = arr[len(arr) // 2]
        return sum(abs(v - m) // x for v in arr)

