class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxFreeTime(self, eventTime, startTime, endTime):
        n = len(startTime)
        gaps = []
        durations = []
        
        # 1. คำนวณ gaps และความยาวของแต่ละ event
        gaps.append(startTime[0])
        durations.append(endTime[0] - startTime[0])
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
            durations.append(endTime[i] - startTime[i])
        gaps.append(eventTime - endTime[n-1])
        
        # 2. เตรียมข้อมูลเพื่อเช็คว่ามี gap อื่นที่ใหญ่พอจะย้าย event ไปลงไหม
        # ใช้ Prefix และ Suffix Max ของ gaps
        left_max = [0] * (len(gaps) + 1)
        right_max = [0] * (len(gaps) + 1)
        
        for i in range(len(gaps)):
            left_max[i+1] = max(left_max[i], gaps[i])
        for i in range(len(gaps)-1, -1, -1):
            right_max[i] = max(right_max[i+1], gaps[i])
            
        ans = 0
        for i in range(n):
            # ช่องว่างรวมถ้าเราขยับ event i (ซ้าย + ขวา)
            combined_gap = gaps[i] + gaps[i+1]
            event_dur = durations[i]
            
            # กรณีที่ 1: ย้าย event i ไปไว้ที่ gap อื่นที่ไกลออกไป
            # เช็ค gap ที่อยู่ก่อนหน้า i (0 ถึง i-1) หรือ หลัง i+1 (i+2 ถึง n)
            if left_max[i] >= event_dur or right_max[i+2] >= event_dur:
                ans = max(ans, combined_gap + event_dur)
            else:
                # กรณีที่ 2: ย้ายไปที่อื่นไม่ได้ ทำได้แค่ขยับซ้าย/ขวาสุดในช่องตัวเอง
                ans = max(ans, combined_gap)
                
        return ans
