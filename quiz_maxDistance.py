class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        # Iterate through all 4 target diagonal directions (NE, NW, SE, SW)
        for dirs in ["NE", "NW", "SE", "SW"]:
            curr_dist = 0
            bad_moves = 0
            for char in s:
                if char in dirs:
                    curr_dist += 1
                else:
                    curr_dist -= 1
                    bad_moves += 1
                
                # Calculate max possible distance at this step with up to k changes
                # Formula: (Good - Bad) + 2 * min(k, Bad)
                ans = max(ans, curr_dist + 2 * min(k, bad_moves))
        
        return ansclass Solution(object):
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
