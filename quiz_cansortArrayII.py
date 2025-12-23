class Solution(object):
    def canSortArray(self, nums):
        p_max = 0
        c_min, c_max = nums[0], nums[0]
        c_bits = bin(nums[0]).count('1')
        
        for x in nums[1:]:
            bits = bin(x).count('1')
            if bits == c_bits:
                c_min = min(c_min, x)
                c_max = max(c_max, x)
            else:
                if p_max > c_min: return False
                p_max = c_max
                c_min, c_max = x, x
                c_bits = bits
                
        return p_max <= c_min
