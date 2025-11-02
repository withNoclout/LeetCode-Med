class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        t = 1
        while True:
            if memory1 < t and memory2 < t:
                return [t, memory1, memory2]
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1
