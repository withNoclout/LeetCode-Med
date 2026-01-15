class Solution(object):
    def countArrays(self, original, bounds):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # กำหนดช่วงที่เป็นไปได้ของ a[0] (low, high)
        low, high = bounds[0]
        
        # d[i] = a[i] - a[0] = original[i] - original[0]
        curr_diff = 0
        for i in range(1, len(original)):
            curr_diff += original[i] - original[i-1]
            # จาก l[i] <= a[i] <= r[i] 
            # จะได้ l[i] <= a[0] + curr_diff <= r[i]
            # ดังนั้น l[i] - curr_diff <= a[0] <= r[i] - curr_diff
            low = max(low, bounds[i][0] - curr_diff)
            high = min(high, bounds[i][1] - curr_diff)
            
        return max(0, high - low + 1)
