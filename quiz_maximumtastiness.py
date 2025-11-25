class Solution(object):
    def maximumTastiness(self, price, k):
        price.sort()
        
        def check(mid):
            count = 1
            last = price[0]
            for p in price:
                if p - last >= mid:
                    count += 1
                    last = p
            return count >= k
            
        left, right = 0, price[-1] - price[0]
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
