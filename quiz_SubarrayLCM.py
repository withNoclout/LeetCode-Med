class Solution(object):
    def subarrayLCM(self, nums, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return (a * b) // gcd(a, b)
            
        n = len(nums)
        res = 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                curr = lcm(curr, nums[j])
                if curr == k:
                    res += 1
                elif curr > k:
                    break
        return res
