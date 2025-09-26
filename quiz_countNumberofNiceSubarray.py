class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Convert nums to 1 if odd, else 0
        prefix = {0: 1}
        count = 0
        cur = 0
        for x in nums:
            cur += x % 2
            if cur - k in prefix:
                count += prefix[cur - k]
            prefix[cur] = prefix.get(cur, 0) + 1
        return count
