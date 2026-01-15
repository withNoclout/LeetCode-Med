import heapq

class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums1)
        # เก็บข้อมูล (ค่าใน nums1, index เดิม, ค่าใน nums2) และเรียงลำดับตาม nums1
        sorted_indices = sorted(range(n), key=lambda i: nums1[i])
        
        ans = [0] * n
        min_heap = []
        current_sum = 0
        
        j = 0
        for i in range(n):
            curr_idx = sorted_indices[i]
            
            # เลื่อน j เพื่อหาตัวที่มีค่าน้อยกว่า nums1[curr_idx] อย่างเข้มงวด
            while j < i and nums1[sorted_indices[j]] < nums1[curr_idx]:
                val2 = nums2[sorted_indices[j]]
                heapq.heappush(min_heap, val2)
                current_sum += val2
                
                if len(min_heap) > k:
                    current_sum -= heapq.heappop(min_heap)
                j += 1
            
            # กรณีที่ค่า nums1 เท่ากัน ต้องใช้ sum เดียวกันที่คำนวณไว้ก่อนหน้า j
            # แต่ในที่นี้ logic j < i และ nums1[j] < nums1[i] จะจัดการให้เอง
            ans[curr_idx] = current_sum
            
        return ans
