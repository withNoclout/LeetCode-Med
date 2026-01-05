from itertools import permutations

class Solution(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        for p in permutations(nums):
            binary_concat = "".join(bin(num)[2:] for num in p)
            max_num = max(max_num, int(binary_concat, 2))
        return max_num
