class Solution(object):
    def minOperations(self, nums):
        import collections
        counts = collections.Counter(nums)
        res = 0
        
        for c in counts.values():
            if c == 1:
                return -1
            res += (c + 2) // 3
            
        return res
