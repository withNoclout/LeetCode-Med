class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # Count how many numbers fall in each residue class mod `value`.
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1  # Python's % is always non-negative

        # Greedily assign integers starting from 0:
        # use one number from residue (i % value) to make i, if available.
        i = 0
        while True:
            r = i % value
            if cnt[r] == 0:
                return i
            cnt[r] -= 1
            i += 1
