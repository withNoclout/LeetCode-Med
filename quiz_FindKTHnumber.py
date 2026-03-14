class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        curr = 1
        k -= 1
        
        while k > 0:
            steps = 0
            first = curr
            last = curr + 1
            
            # Count the steps (numbers) under the current prefix tree
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
                
            if steps <= k:
                # The kth number is not in this subtree, move to next sibling
                curr += 1
                k -= steps
            else:
                # The kth number is in this subtree, move down to first child
                curr *= 10
                k -= 1
                
        return curr
