class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Since nums is sorted, we can group nodes into connected components.
        # A path exists between u and v if and only if all adjacent pairs 
        # between them (in the sorted array) have a difference <= maxDiff.
        # This means they must belong to the same connected component.
        
        groups = [0] * n
        current_group = 0
        
        for i in range(1, n):
            # If the gap between adjacent elements exceeds maxDiff, 
            # the connection breaks and a new component starts.
            if nums[i] - nums[i-1] > maxDiff:
                current_group += 1
            groups[i] = current_group
            
        # For each query, simply check if both nodes are in the same group.
        return [groups[u] == groups[v] for u, v in queries]
