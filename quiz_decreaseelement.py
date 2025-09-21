class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def helper(parity):
            moves = 0
            for i in range(n):
                if i % 2 == parity:
                    left = nums[i - 1] if i - 1 >= 0 else float('inf')
                    right = nums[i + 1] if i + 1 < n else float('inf')
                    need = max(0, nums[i] - min(left, right) + 1)
                    moves += need
            return moves

        return min(helper(0), helper(1))
