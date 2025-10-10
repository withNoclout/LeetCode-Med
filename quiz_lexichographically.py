class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        from collections import deque

        def add_op(t):
            arr = list(t)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            return ''.join(arr)

        def rot_op(t):
            k = b % len(t)
            return t[-k:] + t[:-k] if k else t

        seen = set([s])
        q = deque([s])
        best = s

        while q:
            cur = q.popleft()
            if cur < best:
                best = cur

            t1 = add_op(cur)
            if t1 not in seen:
                seen.add(t1)
                q.append(t1)

            t2 = rot_op(cur)
            if t2 not in seen:
                seen.add(t2)
                q.append(t2)

        return best
