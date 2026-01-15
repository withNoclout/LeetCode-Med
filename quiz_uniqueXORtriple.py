class Solution(object):
    def uniqueXorTriplets(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # นับความถี่ของแต่ละตัวเลขเพื่อจัดการเรื่อง Duplicate values
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        
        vals = sorted(cnt.keys())
        val_set = set(vals)
        ans = 0
        
        # Case 1: (0, 0, 0) -> 0 ^ 0 ^ 0 = 0
        if 0 in cnt and cnt[0] >= 3:
            ans += 1
            
        # Case 2: (a, a, 0) -> a ^ a ^ 0 = 0 (โดยที่ a != 0)
        if 0 in cnt:
            for x in vals:
                if x != 0 and cnt[x] >= 2:
                    ans += 1
                    
        # Case 3: (a, b, c) -> a ^ b ^ c = 0 (โดยที่ a < b < c)
        # a ^ b = c
        n = len(vals)
        for i in range(n):
            for j in range(i + 1, n):
                c = vals[i] ^ vals[j]
                if c > vals[j] and c in val_set:
                    ans += 1
                    
        return ans
