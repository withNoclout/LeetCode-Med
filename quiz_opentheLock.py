from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        def neighbors(state):
            s = list(state)
            for i in range(4):
                d = int(s[i])
                for move in (-1, 1):
                    nd = (d + move) % 10
                    yield state[:i] + str(nd) + state[i+1:]

        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            cur, steps = q.popleft()
            for nxt in neighbors(cur):
                if nxt in dead or nxt in visited:
                    continue
                if nxt == target:
                    return steps + 1
                visited.add(nxt)
                q.append((nxt, steps + 1))
        return -1
