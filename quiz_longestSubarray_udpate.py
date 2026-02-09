class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        for i in range(n):
            seen = set()
            odd_cnt = 0
            even_cnt = 0
            
            for j in range(i, n):
                val = nums[j]
                
                # Only process if this number hasn't been seen in the current subarray
                if val not in seen:
                    seen.add(val)
                    if val % 2 == 1:
                        odd_cnt += 1
                    else:
                        even_cnt += 1
                
                # Check if the subarray nums[i...j] is balanced
                if odd_cnt == even_cnt:
                    ans = max(ans, j - i + 1)
                    
        return ans
