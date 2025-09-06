class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        seen = [False] * n
        stack = [0]
        seen[0] = True
        while stack:
            u = stack.pop()
            for v in rooms[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        return all(seen)
