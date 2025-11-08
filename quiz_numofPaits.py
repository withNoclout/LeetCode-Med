from collections import Counter

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        count = Counter(nums)
        ans = 0

        for x in nums:
            if not target.startswith(x):
                continue
            y = target[len(x):]
            if y in count:
                ans += count[y]
                if x == y:
                    ans -= 1  # cannot use the same element twice
        return ans
