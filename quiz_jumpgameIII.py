class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = [False] * n

        from collections import deque
        q = deque([start])
        visited[start] = True

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for nxt in [i + arr[i], i - arr[i]]:
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        return False
