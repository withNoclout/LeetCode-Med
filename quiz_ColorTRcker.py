class Solution(object):
    def colorTheArray(self, n, queries):
        nums = [0] * n
        res = []
        count = 0
        for i, color in queries:
            if nums[i] != 0:
                if i > 0 and nums[i] == nums[i-1]: count -= 1
                if i < n - 1 and nums[i] == nums[i+1]: count -= 1
            
            nums[i] = color
            
            if i > 0 and nums[i] == nums[i-1]: count += 1
            if i < n - 1 and nums[i] == nums[i+1]: count += 1
            
            res.append(count)
        return res
