class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        n = len(stones)
        max_move = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
        min_move = n
        left = 0
        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1
            if right - left + 1 == n - 1 and stones[right] - stones[left] + 1 == n - 1:
                min_move = min(min_move, 2)
            else:
                min_move = min(min_move, n - (right - left + 1))
        return [min_move, max_move]
