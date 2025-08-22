class Solution(object):
    def findSubsequences(self, nums):
        res = []
        
        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res
