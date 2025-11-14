class Solution(object):
    def sortJumbled(self, mapping, nums):
        def mapped_value(num):
            mapped = ''.join(str(mapping[int(d)]) for d in str(num))
            return int(mapped)

        return sorted(nums, key=lambda x: mapped_value(x))
