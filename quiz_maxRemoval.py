import collections

class Solution(object):
    def maxRemovals(self, source, pattern, targetIndices):
        """
        :type source: str
        :type pattern: str
        :type targetIndices: List[int]
        :rtype: int
        """
        m = len(pattern)
        # dp[j] stores the minimum number of target indices used to form pattern[:j]
        dp = [float('inf')] * (m + 1)
        dp[0] = 0
        
        target_set = set(targetIndices)
        
        # Optimization: Map each character in pattern to its 1-based indices
        p_indices = collections.defaultdict(list)
        for idx, char in enumerate(pattern):
            p_indices[char].append(idx + 1)
            
        for i, char in enumerate(source):
            cost = 1 if i in target_set else 0
            
            # If current source char exists in pattern, try to extend matches
            if char in p_indices:
                # Iterate in reverse to prevent using the same source char for multiple pattern chars
                for j in reversed(p_indices[char]):
                    if dp[j-1] != float('inf'):
                        dp[j] = min(dp[j], dp[j-1] + cost)
                        
        return len(targetIndices) - dp[m]
