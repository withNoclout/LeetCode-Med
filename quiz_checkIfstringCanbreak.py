class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)

        # Check if s1 can break s2
        def can_break(a, b):
            return all(x >= y for x, y in zip(a, b))

        return can_break(s1_sorted, s2_sorted) or can_break(s2_sorted, s1_sorted)
