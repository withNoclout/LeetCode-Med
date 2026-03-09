class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # Step 1: Calculate Prefix Sums
        # prefix[i] is the sum of nums[0...i-1]
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
            
        def merge_sort(lo, hi):
            # Base case: only one element in the range
            if hi - lo <= 1:
                return 0
            
            mid = (lo + hi) // 2
            # Recursively count pairs in left and right halves
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            # Step 2: Count cross-pairs between left and right halves
            # For each prefix[i] in the left half, we find the range [j_low, j_high) 
            # in the right half such that lower <= prefix[j] - prefix[i] <= upper
            j_low = j_high = mid
            for i in range(lo, mid):
                while j_low < hi and prefix[j_low] - prefix[i] < lower:
                    j_low += 1
                while j_high < hi and prefix[j_high] - prefix[i] <= upper:
                    j_high += 1
                count += (j_high - j_low)
                
            # Step 3: Standard merge to keep prefix array sorted
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return merge_sort(0, len(prefix))
