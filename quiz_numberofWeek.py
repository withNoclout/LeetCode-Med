class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total = sum(milestones)
        mx = max(milestones)
        rest = total - mx
        return total if mx <= rest + 1 else 2 * rest + 1
