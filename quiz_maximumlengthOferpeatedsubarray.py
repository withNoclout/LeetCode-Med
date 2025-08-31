class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        if n == 0 or m == 0:
            return 0
        # dp[j] = length of common subarray ending at nums1[i-1] and nums2[j-1]
        dp = [0] * (m + 1)
        ans = 0
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                tmp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                    if dp[j] > ans:
                        ans = dp[j]
                else:
                    dp[j] = 0
                prev = tmp
        return ans
        
