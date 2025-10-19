class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Each nums[i] can be shifted to any integer in [nums[i]-k, nums[i]+k] once.
        # Greedy: sort and assign the smallest available integer for each interval
        # that's > last assigned. If that value is within the interval, we can make
        # this element distinct; otherwise we can't.
        nums.sort()
        ans = 0
        last = -10**20  # last assigned value

        for x in nums:
            lo = x - k
            hi = x + k
            assign = max(last + 1, lo)
            if assign <= hi:
                ans += 1
                last = assign
            # else: this interval sits entirely before (last+1); skip

        return ans
