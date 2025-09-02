class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = Counter(answers)
        res = 0
        for x, c in cnt.items():
            groups = (c + x) // (x + 1)  # number of groups needed
            res += groups * (x + 1)
        return res
