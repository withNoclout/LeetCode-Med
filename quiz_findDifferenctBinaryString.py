class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
