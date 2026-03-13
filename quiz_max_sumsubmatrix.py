import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])
        max_sum = float('-inf')

        # We iterate based on the smaller dimension to optimize
        # Usually, we assume columns are the smaller dimension for outer loops
        for l in range(cols):
            row_sums = [0] * rows
            for r in range(l, cols):
                for i in range(rows):
                    row_sums[i] += matrix[i][r]
                
                # Now find the max subarray sum <= k in row_sums
                # Use a sorted list to simulate a balanced BST for binary search
                prefix_sums = [0]
                current_prefix_sum = 0
                
                for s in row_sums:
                    current_prefix_sum += s
                    
                    # Target: current_prefix_sum - previous_prefix_sum <= k
                    # Rearranged: previous_prefix_sum >= current_prefix_sum - k
                    target = current_prefix_sum - k
                    idx = bisect.bisect_left(prefix_sums, target)
                    
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, current_prefix_sum - prefix_sums[idx])
                    
                    # Optimization: if we hit k exactly, we can't do better
                    if max_sum == k:
                        return k
                    
                    bisect.insort(prefix_sums, current_prefix_sum)
                    
        return max_sum
