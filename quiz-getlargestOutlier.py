from collections import Counter

class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        freq = Counter(nums)
        ans = float('-inf')
        
        # The logic: Total Sum = Sum of Originals + Sum Element + Outlier
        # Since Sum of Originals == Sum Element, 
        # Total Sum = 2 * Sum Element + Outlier
        # Therefore: (Total Sum - Outlier) / 2 = Sum Element
        
        for num in nums:
            # Treat 'num' as the potential outlier
            remaining = total - num
            
            if remaining % 2 == 0:
                target_sum = remaining // 2
                
                if target_sum in freq:
                    # If the calculated sum element is the same number as the outlier candidate,
                    # we need at least 2 occurrences of it in the array.
                    if target_sum != num or freq[target_sum] > 1:
                        ans = max(ans, num)
                        
        return ans
