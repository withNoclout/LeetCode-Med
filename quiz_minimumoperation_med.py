from collections import deque

class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        if start == goal:
            return 0

        q = deque([(start, 0)])
        seen = [False] * 1001  # only track states in [0,1000]
        if 0 <= start <= 1000:
            seen[start] = True

        while q:
            x, d = q.popleft()
            for a in nums:
                for y in (x + a, x - a, x ^ a):
                    if y == goal:
                        return d + 1
                    if 0 <= y <= 1000 and not seen[y]:
                        seen[y] = True
                        q.append((y, d + 1))
        return -1
