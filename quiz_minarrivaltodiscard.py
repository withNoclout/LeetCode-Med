from collections import Counter

class Solution(object):
    def minArrivalsToDiscard(self, arrivals, w, m):
        """
        :type arrivals: List[int]
        :type w: int
        :type m: int
        :rtype: int
        """
        cnt = Counter()
        n = len(arrivals)
        marked = [0] * n
        ans = 0
        
        for i, x in enumerate(arrivals):
            # Remove element leaving the window
            if i >= w:
                prev_idx = i - w
                # Only decrement count if the element leaving was actually kept
                if marked[prev_idx]:
                    cnt[arrivals[prev_idx]] -= 1
            
            # Check if adding current element violates limit m
            if cnt[x] >= m:
                ans += 1
            else:
                marked[i] = 1
                cnt[x] += 1
                
        return ans
