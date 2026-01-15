class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(s)
        # แปลง string เป็นตัวเลข (1 สำหรับ '1', -1 สำหรับ '0')
        # เพื่อใช้เทคนิค Prefix Sum ในการหาจุดสมดุล
        nums = [1 if c == '1' else -1 for c in s]
        
        # ค้นหาค่าสูงสุดของผลรวมสะสมในช่วงที่ต่อเนื่องกัน (Maximum Subarray Sum)
        # หรือจัดการตามเงื่อนไขเฉพาะของ Quiz 3499
        max_active = 0
        current_sum = 0
        min_prefix = 0
        
        prefix_sum = 0
        for x in nums:
            prefix_sum += x
            max_active = max(max_active, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)
            
        return max_active
