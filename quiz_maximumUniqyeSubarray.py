class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        cur = 0
        best = 0

        for right, x in enumerate(nums):
            while x in seen:
                seen.remove(nums[left])
                cur -= nums[left]
                left += 1
            seen.add(x)
            cur += x
            if cur > best:
                best = cur

        return best
