class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def get_max_gap(bars):
            bars.sort()
            max_len = 1
            curr = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    curr += 1
                else:
                    curr = 1
                max_len = max(max_len, curr)
            return max_len + 1
            
        side = min(get_max_gap(hBars), get_max_gap(vBars))
        return side * side
