class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Option 1: Calculate cost without reordering
        # We just modify elements at their current positions
        cost_no_reorder = sum(abs(x - y) for x, y in zip(arr, brr))
        
        # Option 2: Pay 'k' to rearrange 'arr' optimally
        # The optimal arrangement to minimize sum of absolute differences 
        # is when both arrays are sorted.
        arr.sort()
        brr.sort()
        cost_with_reorder = k + sum(abs(x - y) for x, y in zip(arr, brr))
        
        return min(cost_no_reorder, cost_with_reorder)
