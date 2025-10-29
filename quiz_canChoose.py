class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        for g in groups:
            found = False
            while i + len(g) <= len(nums):
                if nums[i:i+len(g)] == g:
                    i += len(g)
                    found = True
                    break
                i += 1
            if not found:
                return False
        return True
