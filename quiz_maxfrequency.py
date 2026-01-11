class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        base_k = nums.count(k)
        max_gain = 0
        
        for target in set(nums):
            if target == k: continue
            current_gain = 0
            local_max = 0
            for x in nums:
                if x == target: current_gain += 1
                elif x == k: current_gain -= 1
                if current_gain < 0: current_gain = 0
                local_max = max(local_max, current_gain)
            max_gain = max(max_gain, local_max)
            
        return base_k + max_gain
