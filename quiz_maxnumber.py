class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        res = []

        # Find the max sub-sequence of length x from a single array
        def getMaxSubsequence(nums, x):
            stack = []
            drop = len(nums) - x
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:x]

        # Merge two sub-sequences to form the maximum possible result
        def merge(s1, s2):
            # Using list comparison s1[i:] > s2[j:] handles look-ahead logic
            return [max(s1, s2).pop(0) for _ in range(k)]

        # Iterate through all valid split points for k
        for i in range(max(0, k - n), min(k, m) + 1):
            s1 = getMaxSubsequence(nums1, i)
            s2 = getMaxSubsequence(nums2, k - i)
            # Maintain the global maximum sequence found
            res = max(res, merge(s1, s2))
            
        return res
