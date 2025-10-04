class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.sort()
        verticalCuts.sort()

        # add edges
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        max_h = max(horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1))
        max_w = max(verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts) - 1))

        return (max_h * max_w) % (10**9 + 7)
