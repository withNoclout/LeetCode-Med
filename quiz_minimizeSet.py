class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        lcm = (divisor1 * divisor2) // gcd(divisor1, divisor2)
        
        left, right = 1, 10**10
        while left < right:
            mid = (left + right) // 2
            cnt1 = mid - mid // divisor1
            cnt2 = mid - mid // divisor2
            total = mid - mid // lcm
            
            if cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and total >= uniqueCnt1 + uniqueCnt2:
                right = mid
            else:
                left = mid + 1
        return left
