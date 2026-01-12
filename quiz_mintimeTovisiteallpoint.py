class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        total_time = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            next_x, next_y = points[i + 1]
            # ระยะทางที่สั้นที่สุดในการเคลื่อนที่ 8 ทิศทาง (Chebyshev Distance)
            total_time += max(abs(next_x - curr_x), abs(next_y - curr_y))
            
        return total_time
