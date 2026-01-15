class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(s)
        # dp[i][j][m] = ความยาว LPS ของ s[i...j] โดยใช้ operations ไป m ครั้ง
        # ใช้ 2D DP เพื่อประหยัด memory (i, j) และวนลูป m
        dp = [[0] * n for _ in range(n)]
        
        # คํานวณ cost ในการเปลี่ยนตัวอักษร a เป็น b (ทิศทางเดียวหรือย้อนกลับ)
        def get_cost(c1, c2):
            v1, v2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            dist = abs(v1 - v2)
            return min(dist, 26 - dist)

        # Base case: subsequence ยาว 1
        memo = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                for m in range(k + 1):
                    if i == j:
                        memo[i][j][m] = 1
                        continue
                    
                    # กรณีไม่เลือกตัวขอบ
                    res = max(memo[i+1][j][m], memo[i][j-1][m])
                    
                    # กรณีเลือกตัวขอบ s[i] และ s[j] มาคู่กัน
                    cost = get_cost(s[i], s[j])
                    if m >= cost:
                        res = max(res, (memo[i+1][j-1][m-cost] if i+1 <= j-1 else 0) + 2)
                    
                    memo[i][j][m] = res
                    
        return memo[0][n-1][k]
