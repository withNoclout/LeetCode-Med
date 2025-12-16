class Solution(object):
    def longestEqualSubarray(self, nums, k):
        import collections
        pos = collections.defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
            
        res = 0
        for indices in pos.values():
            left = 0
            for right in range(len(indices)):
                # span = indices[right] - indices[left] + 1
                # count = right - left + 1
                # deleted = span - count = (indices[right] - indices[left]) - (right - left)
                while (indices[right] - indices[left]) - (right - left) > k:
                    left += 1
                res = max(res, right - left + 1)
                
        return res
