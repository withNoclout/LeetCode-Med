from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        for num in sorted(count.keys()):
            while count[num] > 0:
                for i in range(k):
                    if count[num + i] <= 0:
                        return False
                    count[num + i] -= 1
        return True
