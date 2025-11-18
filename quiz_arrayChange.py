class Solution(object):
    def arrayChange(self, nums, operations):
        pos = {v: i for i, v in enumerate(nums)}
        
        for a, b in operations:
            i = pos[a]
            nums[i] = b
            pos[b] = i
            del pos[a]
        
        return nums
