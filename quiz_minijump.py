from collections import deque

class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        forb = set(forbidden)
        limit = max([x] + forbidden) + a + b

        q = deque()
        q.append((0, 0))  # (position, used_back) where used_back=1 if last move was backward
        visited = set([(0, 0)])

        steps = 0
        while q:
            for _ in range(len(q)):
                pos, used_back = q.popleft()
                if pos == x:
                    return steps

                # forward jump
                npos = pos + a
                if 0 <= npos <= limit and npos not in forb and (npos, 0) not in visited:
                    visited.add((npos, 0))
                    q.append((npos, 0))

                # backward jump (only if previous move wasn't backward)
                if used_back == 0:
                    npos = pos - b
                    if 0 <= npos and npos not in forb and (npos, 1) not in visited:
                        visited.add((npos, 1))
                        q.append((npos, 1))
            steps += 1

        return -1
