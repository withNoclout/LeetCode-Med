class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        ans = 0

        # from bottom up to just before first special
        ans = max(ans, special[0] - bottom)

        # between specials
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)

        # from after last special to top
        ans = max(ans, top - special[-1])

        return ans
