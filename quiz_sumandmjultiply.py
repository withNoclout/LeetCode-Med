import sys

# Increase recursion depth for deep Segment Trees in Python
sys.setrecursionlimit(200000)

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Precompute Prefix Sums for digit summation
        # P[i] stores sum of digits in s[0...i-1]
        P = [0] * (n + 1)
        curr = 0
        for i in range(n):
            curr += int(s[i])
            P[i+1] = curr
            
        # 2. Precompute Powers of 10 for O(1) shifting
        # powers[k] = 10^k % MOD
        powers = [1] * (n + 1)
        curr_pow = 1
        for i in range(1, n + 1):
            curr_pow = (curr_pow * 10) % MOD
            powers[i] = curr_pow
            
        # 3. Segment Tree Setup
        # tree_val[node]: integer value formed by non-zero digits in the node's range
        # tree_cnt[node]: count of non-zero digits in the node's range
        tree_val = [0] * (4 * n)
        tree_cnt = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                digit = int(s[start])
                if digit == 0:
                    tree_val[node] = 0
                    tree_cnt[node] = 0
                else:
                    tree_val[node] = digit
                    tree_cnt[node] = 1
                return

            mid = (start + end) // 2
            left = 2 * node
            right = 2 * node + 1
            
            build(left, start, mid)
            build(right, mid + 1, end)
            
            # Merge Logic:
            # Combine left and right parts. The left part is shifted by 
            # 10^(count of non-zeros in right part).
            r_count = tree_cnt[right]
            tree_val[node] = (tree_val[left] * powers[r_count] + tree_val[right]) % MOD
            tree_cnt[node] = tree_cnt[left] + r_count

        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0, 0
            
            if l <= start and end <= r:
                return tree_val[node], tree_cnt[node]
            
            mid = (start + end) // 2
            
            # Optimization: If query fits entirely in one child, don't split unnecessarily
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            if l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            
            # If split across both children, merge the results
            v1, c1 = query(2 * node, start, mid, l, r)
            v2, c2 = query(2 * node + 1, mid + 1, end, l, r)
            
            combined_val = (v1 * powers[c2] + v2) % MOD
            combined_cnt = c1 + c2
            return combined_val, combined_cnt

        # Build the Segment Tree
        build(1, 0, n - 1)
        
        ans = []
        for l, r in queries:
            # Step A: Get Sum of Digits in range (O(1))
            digit_sum = P[r+1] - P[l]
            
            if digit_sum == 0:
                # If sum is 0, x must also be 0 (no non-zero digits), so result is 0
                ans.append(0)
                continue
            
            # Step B: Get Concatenated Value 'x' from Tree (O(log N))
            x_val, _ = query(1, 0, n - 1, l, r)
            
            # Step C: Calculate Final Result
            result = (x_val * digit_sum) % MOD
            ans.append(result)
            
        return ans
