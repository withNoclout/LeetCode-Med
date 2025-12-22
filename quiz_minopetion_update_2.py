class Solution(object):
    def minOperations(self, nums1, nums2):
        n = len(nums1)
        
        def solve(target1, target2):
            count = 0
            for i in range(n - 1):
                if nums1[i] <= target1 and nums2[i] <= target2:
                    continue
                elif nums1[i] <= target2 and nums2[i] <= target1:
                    count += 1
                else:
                    return float('inf')
            return count

        # Option 1: Don't swap the last elements
        res1 = solve(nums1[-1], nums2[-1])
        
        # Option 2: Swap the last elements
        res2 = solve(nums2[-1], nums1[-1]) + 1
        
        ans = min(res1, res2)
        return ans if ans != float('inf') else -1
