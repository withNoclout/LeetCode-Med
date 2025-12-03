class Solution(object):
    def countTrapezoids(self, points):
        from collections import defaultdict
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        lines = defaultdict(lambda: defaultdict(int))
        midpoints = defaultdict(lambda: defaultdict(int))
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dy = y2 - y1
                dx = x2 - x1
                g = gcd(abs(dy), abs(dx))
                dy //= g
                dx //= g
                
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                
                slope = (dy, dx)
                intercept = dx * y1 - dy * x1
                lines[slope][intercept] += 1
                
                midpoints[(x1 + x2, y1 + y2)][slope] += 1
        
        MOD = 10**9 + 7
        total_candidates = 0
        
        for intercepts in lines.values():
            total_segments = sum(intercepts.values())
            count = total_segments * (total_segments - 1) // 2
            for k in intercepts.values():
                count -= k * (k - 1) // 2
            total_candidates = (total_candidates + count) % MOD
            
        total_parallelograms = 0
        for slopes in midpoints.values():
            total_segments = sum(slopes.values())
            count = total_segments * (total_segments - 1) // 2
            for k in slopes.values():
                count -= k * (k - 1) // 2
            total_parallelograms = (total_parallelograms + count) % MOD
            
        return (total_candidates - total_parallelograms + MOD) % MOD
