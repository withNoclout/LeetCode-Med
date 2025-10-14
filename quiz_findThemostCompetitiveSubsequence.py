class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Greedy monotonic stack.
        # We can delete at most (n - k) elements to keep the subsequence length k.
        removes = len(nums) - k
        stack = []
        for x in nums:
            while stack and removes > 0 and stack[-1] > x:
                stack.pop()
                removes -= 1
            stack.append(x)
        # If we didn't exhaust removals, simply take the first k elements.
        return stack[:k]
