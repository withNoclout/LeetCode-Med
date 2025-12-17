class Solution(object):
    def minLengthAfterRemovals(self, nums):
        n = len(nums)
        import collections
        counts = collections.Counter(nums)
        max_freq = max(counts.values())
        
        if max_freq > n // 2:
            return 2 * max_freq - n
        
        return n % 2
