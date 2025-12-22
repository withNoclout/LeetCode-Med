class Solution(object):
    def distributeCandies(self, n, limit):
        def count(target):
            if target < 0: return 0
            return (target + 2) * (target + 1) // 2
            
        lim = limit + 1
        res = count(n)
        res -= 3 * count(n - lim)
        res += 3 * count(n - 2 * lim)
        res -= count(n - 3 * lim)
        
        return res
