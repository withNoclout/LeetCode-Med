from collections import defaultdict

class Solution(object):
    def prefixConnected(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: int
        """
        # Dictionary to count the frequency of each prefix
        prefix_counts = defaultdict(int)
        
        for word in words:
            # Words shorter than k cannot form a valid prefix group
            if len(word) < k:
                continue
            
            # Extract the prefix of length k
            prefix = word[:k]
            prefix_counts[prefix] += 1
            
        ans = 0
        # Check each unique prefix group
        for count in prefix_counts.values():
            # A valid group must have at least two words
            if count >= 2:
                ans += 1
                
        return ans
