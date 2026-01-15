class Solution(object):
    def largestPrimeSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        
        # 1. ใช้ Sieve of Eratosthenes เพื่อหาและตรวจสอบ Prime ในช่วง [0, n]
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        limit = int(n**0.5)
        for i in range(2, limit + 1):
            if is_prime[i]:
                # Slice assignment เพื่อความเร็วในการตัดตัวประกอบ
                is_prime[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))
        
        # 2. สร้างรายการ Prime เพื่อนำมาหาผลรวมสะสม
        primes = [i for i, prime in enumerate(is_prime) if prime]
        
        max_ans = 0
        curr_sum = 0
        
        # 3. วนลูปหาผลรวมสะสม (Prefix Sum) ของจำนวนเฉพาะเริ่มจาก 2
        for p in primes:
            curr_sum += p
            
            # ถ้าผลรวมเกิน n ให้หยุดทันที
            if curr_sum > n:
                break
            
            # เช็คว่าผลรวมนั้นเป็นจำนวนเฉพาะหรือไม่
            if is_prime[curr_sum]:
                max_ans = curr_sum
                
        return max_ans
