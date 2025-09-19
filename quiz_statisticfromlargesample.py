class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        # There are 256 possible values (0-255)
        n = len(count)
        total = sum(count)
        minimum = next(i for i, c in enumerate(count) if c > 0)
        maximum = next(i for i in range(n-1, -1, -1) if count[i] > 0)
        # Mean
        mean = sum(i * count[i] for i in range(n)) / float(total)
        # Mode
        mode = max(range(n), key=lambda i: count[i])
        # Median
        mid1 = (total + 1) // 2
        mid2 = (total + 2) // 2
        m1 = m2 = None
        cnt = 0
        for i in range(n):
            cnt += count[i]
            if m1 is None and cnt >= mid1:
                m1 = i
            if m2 is None and cnt >= mid2:
                m2 = i
                break
        median = (m1 + m2) / 2.0
        return [float(minimum), float(maximum), mean, median, float(mode)]
